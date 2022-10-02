#coding=utf-8
from xml.dom.minidom import Document    #使用这个工具来读写xml
import random
class URDF_GEN:

    def __init__(self,name='unamed'):
        '''配置机器人'''
        objNums = 0  # 每新建一个元件id就+1
        self.doc=Document()    #机器人的描述性文件
        self.robot=self.doc.createElement("robot")
        self.robot.setAttribute('name',name)
        self.tree={}
    def Add_Cylinder(self,name='',
                     len=0.0,
                     radius=0.0,
                     father='',
                     origin_xyz='0.0 0.0 0.0',
                     origin_rpy='0.0 0.0 0.0',
                     rgba="1 1 1 1"
                     ):
        '''添加一个圆柱形'''
        if father=='': father=self.robot
        subLink=self.doc.createElement('link')
        subLink.setAttribute('name', name)

        #visual部分
        visual = self.doc.createElement('visual')

        #geometry部分
        geom = self.doc.createElement('geometry')
        cyln = self.doc.createElement('cylinder')
        cyln.setAttribute('length',str(len))
        cyln.setAttribute('radius', str(radius))
        geom.appendChild(cyln)
        visual.appendChild(geom)
        #material部分
        material = self.doc.createElement('material')
        color = self.doc.createElement('color')
        material.setAttribute('name', 'color_'+str(int(random.random()*10000)))
        color.setAttribute('rgba', rgba)
        material.appendChild(color)
        visual.appendChild(material)
        #origin部分
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        visual.appendChild(origin)
        #collision
        geom = self.doc.createElement('geometry')
        cyln = self.doc.createElement('cylinder')
        cyln.setAttribute('length', str(len))
        cyln.setAttribute('radius', str(radius))
        geom.appendChild(cyln)
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        coll = self.doc.createElement('collision')
        coll.appendChild(geom)
        coll.appendChild(origin)

        #添加
        subLink.appendChild(visual)
        subLink.appendChild(coll)
        father.appendChild(subLink)
    def Add_Cube(self,name='',
                     sSize='0 0 0',
                     father='',
                     origin_xyz='0.0 0.0 0.0',
                     origin_rpy='0.0 0.0 0.0',
                     rgba="1 1 1 1"
                     ):
        '''添加一个长方形'''
        if father == '': father = self.robot
        subLink = self.doc.createElement('link')
        subLink.setAttribute('name', name)

        # visual部分
        visual = self.doc.createElement('visual')

        # geometry部分
        geom = self.doc.createElement('geometry')
        bbx = self.doc.createElement('box')
        bbx.setAttribute('size', sSize)
        geom.appendChild(bbx)
        visual.appendChild(geom)
        # material部分
        material = self.doc.createElement('material')
        color = self.doc.createElement('color')
        material.setAttribute('name', 'color_' + str(int(random.random() * 10000)))
        color.setAttribute('rgba', rgba)
        material.appendChild(color)
        visual.appendChild(material)
        # origin部分
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        visual.appendChild(origin)
        # collision
        geom = self.doc.createElement('geometry')
        bbx = self.doc.createElement('box')
        bbx.setAttribute('size', sSize)
        geom.appendChild(bbx)
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        coll = self.doc.createElement('collision')
        coll.appendChild(geom)
        coll.appendChild(origin)

        # 添加
        subLink.appendChild(visual)
        subLink.appendChild(coll)
        father.appendChild(subLink)
    def Add_Mesh(self,name='',
                     meshFile='',
                     father='',
                     origin_xyz='0.0 0.0 0.0',
                     origin_rpy='0.0 0.0 0.0',
                     rgba="1 1 1 1"
                     ):
        '''添加一个圆柱形'''
        '''添加一个球形'''
        if father == '': father = self.robot
        subLink = self.doc.createElement('link')
        subLink.setAttribute('name', name)

        # visual部分
        visual = self.doc.createElement('visual')

        # geometry部分
        geom = self.doc.createElement('geometry')
        mesh = self.doc.createElement('mesh')
        mesh.setAttribute('filename', meshFile)
        geom.appendChild(mesh)
        visual.appendChild(geom)
        # material部分
        material = self.doc.createElement('material')
        color = self.doc.createElement('color')
        material.setAttribute('name', 'color_' + str(int(random.random() * 10000)))
        color.setAttribute('rgba', rgba)
        material.appendChild(color)
        visual.appendChild(material)
        # origin部分
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        visual.appendChild(origin)
        # collision
        geom = self.doc.createElement('geometry')
        mesh = self.doc.createElement('mesh')
        mesh.setAttribute('filename', meshFile)
        geom.appendChild(mesh)
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        coll = self.doc.createElement('collision')
        coll.appendChild(geom)
        coll.appendChild(origin)

        # 添加
        subLink.appendChild(visual)
        subLink.appendChild(coll)
        father.appendChild(subLink)
    def Add_Cube(self,name='',
                     sSize='0 0 0',
                     father='',
                     origin_xyz='0.0 0.0 0.0',
                     origin_rpy='0.0 0.0 0.0',
                     rgba="1 1 1 1"
                     ):
        '''添加一个长方形'''
        if father == '': father = self.robot
        subLink = self.doc.createElement('link')
        subLink.setAttribute('name', name)

        # visual部分
        visual = self.doc.createElement('visual')

        # geometry部分
        geom = self.doc.createElement('geometry')
        bbx = self.doc.createElement('box')
        bbx.setAttribute('size', sSize)
        geom.appendChild(bbx)
        visual.appendChild(geom)
        # material部分
        material = self.doc.createElement('material')
        color = self.doc.createElement('color')
        material.setAttribute('name', 'color_' + str(int(random.random() * 10000)))
        color.setAttribute('rgba', rgba)
        material.appendChild(color)
        visual.appendChild(material)
        # origin部分
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        visual.appendChild(origin)
        # collision
        geom = self.doc.createElement('geometry')
        bbx = self.doc.createElement('box')
        bbx.setAttribute('size', sSize)
        geom.appendChild(bbx)
        origin = self.doc.createElement('origin')
        origin.setAttribute('rpy', origin_rpy)
        origin.setAttribute('xyz', origin_xyz)
        coll = self.doc.createElement('collision')
        coll.appendChild(geom)
        coll.appendChild(origin)

        # 添加
        subLink.appendChild(visual)
        subLink.appendChild(coll)
        father.appendChild(subLink)
    def Add_Joint(self,name='unamed_J',
                  type='revolute',
                  parent_link='',
                  child_link='',
                  origin_rpy='0 0 0',
                  origin_xyz='0 0 0',
                  axis_xyz='0 0 1',
                  vel=0.5,
                  max=0.785,
                  min=-0.785,
                  effort=1000.0,
                  father=''
                  ):
        '''
            添加一个关节
            :param name:
            :param type:
            :param parent_link:
            :param child_link:
            :param origin_rpy:
            :param origin_xyz:
            :param vel:
            :param max:
            :param min:
        :return:
        '''
        if father == '': father = self.robot
        subJoint = self.doc.createElement('joint')
        subJoint.setAttribute('name', name)
        subJoint.setAttribute('type', type)
        #axis
        axis = self.doc.createElement('axis')
        axis.setAttribute('xyz',axis_xyz)
        subJoint.appendChild(axis)
        # origin
        ori = self.doc.createElement('origin')
        ori.setAttribute('rpy', origin_rpy)
        ori.setAttribute('xyz', origin_xyz)
        subJoint.appendChild(ori)
        #parent/child
        par = self.doc.createElement('parent')
        chi= self.doc.createElement('child')
        par.setAttribute('link',parent_link)
        chi.setAttribute('link',child_link)
        subJoint.appendChild(par)
        subJoint.appendChild(chi)
        if type=='fixed':
            self.robot.appendChild(subJoint)
            return
        #limit
        lim = self.doc.createElement('limit')
        lim.setAttribute('lower', str(min))
        lim.setAttribute('upper', str(max))
        lim.setAttribute('velocity', str(vel))
        lim.setAttribute('effort', str(effort))
        subJoint.appendChild(lim)
        self.robot.appendChild(subJoint)

    def Save(self,fileName='urdf.urdf'):
        self.doc.appendChild(self.robot)
        with open(fileName,'w',encoding='utf-8') as f:
            self.doc.writexml(f,indent='',addindent=' ',newl='\n',encoding='utf-8')

u=URDF_GEN('6dof_arm')  #生成一台机器人

#添加Link
u.Add_Cube(name='base_link',sSize='0.15 0.15 0.005',origin_xyz='0 0 0.0025',rgba='0.8 0.8 0.8 1')   #底座
u.Add_Cylinder(name='arm_base',len=0.065,radius=0.10,origin_xyz='0 0 0.0325',rgba='1.0 0.5 0.0 1')  #机械波的外部圆
u.Add_Cylinder(name='L0',len=0.065,radius=0.08,origin_xyz='0 0 0.035',rgba='0.8 0.5 0.2 1')         #机械臂的内部圆
u.Add_Cube(name='L1',sSize='0.025 0.057 0.106',origin_xyz='0 0 0.053',rgba='0.6 0.5 0.4 1')        #第一条臂
u.Add_Cube(name='L2',sSize='0.025 0.057 0.098',origin_xyz='0 0 0.049',rgba='0.4 0 0.6 1')           #第二条臂
u.Add_Cube(name='L3',sSize='0.05 0.057 0.057',origin_xyz='0.025 0.0 0.0287',rgba='0.2 1 0.8 1')       #第三条臂
u.Add_Cube(name='L4',sSize='0.02 0.05 0.04',origin_xyz='0 0 0.02',rgba='0.0 1 1 1')
u.Add_Cylinder(name='clip',len=0.065,radius=0.01,origin_xyz='0.0 0.0 0.0325')

#添加Joint
u.Add_Joint(name='Jbase',type='fixed',parent_link='base_link',child_link='arm_base',origin_xyz='0 0 0.005')
u.Add_Joint(name='J0',parent_link='arm_base',child_link='L0',axis_xyz='0 0 1',origin_xyz='0 0 0.000',max=2.09,min=-2.09)
u.Add_Joint(name='J1',parent_link='L0',child_link='L1',axis_xyz='0 1 0',origin_xyz='0 0 0.0774',max=2.09,min=-2.09)     #内部圆和机械臂的第一个关节
u.Add_Joint(name='J2',parent_link='L1',child_link='L2',axis_xyz='0 1 0',origin_xyz='0 0 0.105',max=2.09,min=-2.09)      #第一和第二关节
u.Add_Joint(name='J3',parent_link='L2',child_link='L3',axis_xyz='0 1 0',origin_xyz='0 0 0.098',max=2.09,min=-2.09)      #第二和第三关节
u.Add_Joint(name='J4',parent_link='L3',child_link='L4',axis_xyz='0 0 1',origin_xyz='0.031 0.014 0.059',max=2.09,min=-2.09)   #第三和第四关节
u.Add_Joint(name='clip',parent_link='L4',child_link='clip',axis_xyz='1 0 0',origin_xyz='0.015 0.00 0.04',max=1.5,min=-1.5)   #夹子
u.Save()


# u.Add_Mesh(name='base_link',meshFile='package://simulator_bringup/cfg/small_robo.stl',origin_rpy='1.57 0 1.57',origin_xyz='-0.0875 -0.0925 0',rgba='0.9 0.9 0.9 1')   #底座
# u.Add_Cylinder(name='wheel_L',len=0.02,radius=0.06,origin_xyz='0 0 0.0',rgba='0 0 0 1')
# u.Add_Cylinder(name='wheel_R',len=0.02,radius=0.06,origin_xyz='0 0 0.0',rgba='0 0 0 1')
# u.Add_Cylinder(name='laser',len=0.03,radius=0.04,origin_xyz='0 0 0.02',rgba='0 0.0 1.0 1')
# u.Add_Joint(name='base_laser',type='fixed',parent_link='base_link',child_link='laser',origin_xyz='0.0 0 0.15')
# u.Add_Joint(name='base_l_wheel',type='continuous',parent_link='base_link',child_link='wheel_L',origin_xyz='0 -0.0925 0.04',origin_rpy='1.57 0 0')
# u.Add_Joint(name='base_r_wheel',type='continuous',parent_link='base_link',child_link='wheel_R',origin_xyz='0 0.0925 0.04',origin_rpy='-1.57 0 0')
# u.Save()