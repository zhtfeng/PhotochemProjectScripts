

import os
import time
import numpy as np
import re

class Trajectory:

    def __init__(self, coord_list, name, index, atom_list):

        self.coord = np.array(coord_list)
        self.index = index
        self.name = name
        self.attribute = [1]
        self.end_point_name = set()
        self.starting_attribute = [1]
        self.end_point_type = set()

    def distance(self, bond):

        a, b = bond
        distArr = np.array([])

        for point in range(self.time):

            dist = self.dist(a, b, point)
            distArr = np.append(distArr, dist)

        return distArr

    def angle(self, bondangle):

        a, b, c = bondangle
        angle_list = []

        for point in range(self.time):
            ang = self.ang(a, b, c, point)
            angle_list.append(ang)

        return angle_list

    def dihedral(self, dihedralangle):

        a, b, c, d = dihedralangle
        dihedralArr = np.array([])

        for point in range(self.time):
            dih = self.dih(a, b, c, d, point)
            dihedralArr = np.append(dihedralArr, dih)

        return dihedralArr

    def initialize_attribute(self, full):

        self.attribute = self.attribute * full
        self.starting_attribute = self.starting_attribute * full

        return self.attribute, self.starting_attribute

    def dist(self, a, b, point):

        a -= 1
        b -= 1
        cart = self.coord[int(point)]
        dist = np.sqrt((cart[a, 0] - cart[b, 0]) ** 2 + (cart[a, 1] - cart[b, 1]) ** 2 +
                       (cart[a, 2] - cart[b, 2]) ** 2)

        return dist

    def ang(self, a, b, c, point):

        a -= 1
        b -= 1
        c -= 1
        cart = self.coord[int(point)]
        vec_a = np.array([(cart[a, 0] - cart[b, 0]), (cart[a, 1] - cart[b, 1]), (cart[a, 2] - cart[b, 2])])
        vec_b = np.array([(cart[c, 0] - cart[b, 0]), (cart[c, 1] - cart[b, 1]), (cart[c, 2] - cart[b, 2])])
        cos_theta = vec_a.dot(vec_b) / (np.sqrt(vec_a.dot(vec_a) * vec_b.dot(vec_b)))
        theta = np.arccos(cos_theta)
        theta = 180 * theta / np.pi

        return theta

    def dih(self, a, b, c, d, point):

        a -= 1
        b -= 1
        c -= 1
        d -= 1
        cart = self.coord[int(point)]
        vec_a_1 = np.array([(cart[a, 0] - cart[b, 0]), (cart[a, 1] - cart[b, 1]), (cart[a, 2] - cart[b, 2])])
        vec_a_2 = np.array([(cart[c, 0] - cart[b, 0]), (cart[c, 1] - cart[b, 1]), (cart[c, 2] - cart[b, 2])])
        vec_b_1 = np.array([(cart[b, 0] - cart[c, 0]), (cart[b, 1] - cart[c, 1]), (cart[b, 2] - cart[c, 2])])
        vec_b_2 = np.array([(cart[d, 0] - cart[c, 0]), (cart[d, 1] - cart[c, 1]), (cart[d, 2] - cart[c, 2])])
        norm_a = np.cross(vec_a_1, vec_a_2)
        norm_b = np.cross(vec_b_1, vec_b_2)
        cos_theta = norm_a.dot(norm_b) / (np.sqrt(norm_a.dot(norm_a) * norm_b.dot(norm_b)))
        theta = np.arccos(cos_theta)
        theta = 180 * theta / np.pi

        return theta



def process(coord):
    cartesian = np.zeros((len(coord) - 1, 3))
    initial_line = re.split(r' +', coord[0])  # initial line contains several important info about the point
    atom_list = []

    for i in range(1, len(coord)):  # extract out the coordinate of each atom and put it into a list

        line = re.split(r'[\s]', coord[i])
        atom_list.append(line[0])
        line = [x for x in line if x != '']
        cartesian[i - 1, 0] = float(line[1])
        cartesian[i - 1, 1] = float(line[2])
        cartesian[i - 1, 2] = float(line[3])

    return cartesian, initial_line, atom_list


#### similar function for uphill dynamics ####

def get_raw_dyn_uphill(filename):
    read_file = open(filename)
    data = read_file.readlines()
    atm_num = int(data[0])
    temp = []
    traj_coord = []

    for line_num, data_line in enumerate(data):

        if line_num % (atm_num + 2) == 0:

            traj_coord.append(temp)
            temp = []

        else:

            temp.append(data_line)

    traj_coord.pop(0)
    cartesian_list = []

    for each in traj_coord:
        pro = process(each)
        cartesian_list.append(pro[0])

    atom_list = pro[2]  # occurence of errors if QCEIMS traj files are used !!!
    read_file.close()

    return cartesian_list, atom_list


def read_ana_file(directTraj='Specified'):
    global struct_list
    if directTraj == 'Specified':
        ana_file = open('def.txt')
    else:
        ana_file = open(directTraj + 'def.txt')
    ana = ana_file.readlines()
    print('The analyze file has defined ', ana.count('next\n') + 1, ' different outcomes')
    sub_command = []  # criteria of a single structure
    sub_command_lines = []  # collection of structures
    struct_list, type_list = [], []

    for line in ana:

        if line[0:4] == 'next' or line[0:3] == 'end':

            sub_command_lines.append(sub_command)
            sub_command = []

        else:

            sub_command.append(line)

    for sub_index, sub in enumerate(sub_command_lines):

        struct_list.append('Unknown Structure' + str(sub_index))
        type_list.append(None)

        for line in sub:

            line = line.split(' ')
            if line[0] == 'print':
                structure_name = line[1]
                struct_list[sub_index] = structure_name[:-1]

            if line[0] == 'type':
                type_list[sub_index] = line[-1]

    ana_file.close()

    return sub_command_lines, struct_list, type_list


def ana_traj_file(rules, traj):
    traj.initialize_attribute(full=len(rules))  #### Now we apply the criteria to the trajctories ####

    for sub_index, sub in enumerate(rules):

        for line in sub:

            line = line.split(' ')

            if line[0] == 'bond':

                geom_parameter = traj.dist(int(line[1]), int(line[2]), -1)
                starting_geom_parameter = traj.dist(int(line[1]), int(line[2]), 0)

            elif line[0] == 'angle':

                geom_parameter = traj.ang(int(line[1]), int(line[2]), int(line[3]), -1)
                starting_geom_parameter = traj.ang(int(line[1]), int(line[2]), int(line[3]), 0)

            elif line[0] == 'dihedral':

                geom_parameter = traj.dih(int(line[1]), int(line[2]), int(line[3]), int(line[4]), -1)
                starting_geom_parameter = traj.dih(int(line[1]), int(line[2]), int(line[3]), int(line[4]), 0)

            elif line[0] == 'time':

                geom_parameter = float(line[-1])

            if line[-2] == '<':

                if geom_parameter > float(line[-1]):
                    traj.attribute[sub_index] = 0

                if starting_geom_parameter > float(line[-1]):
                    traj.starting_attribute[sub_index] = 0


            elif line[-2] == '>':

                if geom_parameter < float(line[-1]):
                    traj.attribute[sub_index] = 0

                if starting_geom_parameter > float(line[-1]):
                    traj.starting_attribute[sub_index] = 0


def assign_traj(traj, struc_list, type_list):  #### put names on to the trajs, name obtained from print

    if 1 not in traj.attribute:
        traj.end_point_name.add('Unknown')

    if 1 not in traj.starting_attribute:
        traj.end_point_name.add('Unknown')

    for i, j in enumerate(traj.attribute):

        if j == 1:
            traj.end_point_name.add(struc_list[i])
            traj.end_point_type.add(type_list[i])

    for i, j in enumerate(traj.starting_attribute):

        if j == 1:
            traj.end_point_name.add(struc_list[i])
            traj.end_point_type.add(type_list[i])

        traj.end_point_name = set(traj.end_point_name)

def xyz_emptiness_check():
    print('Entering emptiness check')
    if os.path.isfile('output.xyz'):
        print(os.path.getsize('output.xyz'))

        if os.path.getsize('output.xyz') > 1000:

            return True
        else:

            return False
    else:

        return False

index = 0
definitionPath = '/home/zhtfeng/photochem/denitro/DYN-AZ/'
anaRules = read_ana_file(definitionPath) # read in the analysis definition, similar to proganal
monitorfile = open('pyout.txt','w')

while True: # main loop until the criteria reached

    monitorfile = open('pyout.txt', 'a')
    executeXYZCheck = xyz_emptiness_check()
    index += 1
    if executeXYZCheck:


        xyzFilename = 'output.xyz'
        dyn_coord = get_raw_dyn_uphill('output.xyz')
        traj = Trajectory(dyn_coord[0], xyzFilename, index, dyn_coord[1]) # read in the xyz file generated by SHARC
        ana_traj_file(anaRules[0], traj)
        assign_traj(traj, anaRules[1], anaRules[2]) # assigning end point name to the traj, if does not apply to any defined in anaRules, then it will be a set with only one element 'Unknown'
        if len(traj.end_point_name) != 1: # when reached at end point
            status = False # end the loop
            os.system('touch STOP') # tell SHARC it is good to stop
            monitorfile.write('End point reached')
            monitorfile.close()
            break
        monitorfile.write(str(traj.dist(2,5,-1)) + '   \n')
        monitorfile.write('Running point number ' + str(index)+'\n')
        monitorfile.close()

    else:
        print('out of the loop')
        if index > 10:
            print('no response after very long time')
            monitorfile.close()
            break
    time.sleep(200) # execute the next loop a few seconds later














