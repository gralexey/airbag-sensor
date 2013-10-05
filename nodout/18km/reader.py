# -*- coding: cp1251 -*-
#
#	ls-dyna nodout file reader
#
class node_time:
	def __init__ (self):
		self.entity = ''
		self.title = ''
		self.x_disp = []
		self.y_disp = []
		self.z_disp = []
		self.x_vel = []
		self.y_vel = []
		self.z_vel = []
		self.x_accl = []
		self.y_accl = []
		self.z_accl = []
		self.x_coor = []
		self.y_coor = []
		self.z_coor = []
		self.x_rot = []
		self.y_rot = []
		self.z_rot = []
		self.x_rot_vel = []
		self.y_rot_vel = []
		self.z_rot_vel = []
		self.x_rot_accl = []
		self.y_rot_accl = []
		self.z_rot_accl = []
		
		

class lsdyna_reader:
	
	def __init__ (self):
		pass
		
	def nodeout_print_test(self):
		
		for entity, value  in self.nodout.iteritems():
			if entity == '__time':
				print 'time = ', value[-1]
				print
			else:
				print 'entity = ', entity, 'title = ', value.title
				print 'x_disp = ', value.x_disp[-1]
				
				print 'y_disp = ', value.y_disp[-1]
				print 'z_disp = ', value.z_disp[-1]
				"""
				print 'x_vel = ', value.x_vel
				print 'y_vel = ', value.y_vel
				print 'z_vel = ', value.z_vel
				print 'x_accl = ', value.x_accl
				print 'y_accl = ', value.y_accl
				print 'z_accl = ', value.z_accl
				print 'x_coor = ', value.x_coor
				print 'y_coor = ', value.y_coor
				print 'z_coor = ', value.z_coor
				print 'x_rot = ', value.x_rot
				print 'y_rot = ', value.y_rot
				print 'z_rot = ', value.z_rot
				print 'x_rot_vel = ', value.x_rot_vel
				print 'y_rot_vel = ', value.y_rot_vel
				print 'z_rot_vel = ', value.z_rot_vel
				print 'x_rot_accl = ', value.x_rot_accl
				print 'y_rot_accl = ', value.y_rot_accl
				print 'z_rot_accl = ', value.z_rot_accl
				"""
				print
		
		
	def read_nodout (self, file_name):

		self.nodout = dict()
		self.nodout['__time'] = []

		file = open (file_name, "r")
		
		self.read_legend (file)
		self.read_nodout_data(file)
		
	def read_legend (self, file):
		
		line = file.readline()
		line = file.readline()
		line = file.readline()
		line = file.readline()
		line = file.readline()
		line = file.readline()
		line = file.readline()
		line = file.readline()
		while line:
#			print line
			if line.startswith ('{END LEGEND}'):
				break
			entity = line [0:14].strip()
			title  = line [14:70].strip()
										
#			int(entity)
			node = node_time ()
			node.entity = entity
			node.title = title
					
			self.nodout[entity] = node
					
			line = file.readline()
			
			
		line = file.readline()
			
	def read_nodout_data (self, file):
		time_list = self.nodout['__time']
		line = file.readline()
		while line :
#			print line
			if line.startswith (' n o d a l   p r i n t   o u t   f o r   t i m e  s t e p'):
				time = line [105:117].strip()
#				print time
				time_list.append (float(time))
				line = file.readline()
				line = file.readline()
				line = file.readline()
				while line:
					entity = line [0:10].strip()
					if (not self.nodout.has_key (entity) ):
						break
					
					
					x_disp = line [10:22].strip()
					y_disp = line [22:34].strip()
					z_disp = line [34:46].strip()
					x_vel = line [46:58].strip()
					y_vel = line [58:70].strip()
					z_vel = line [70:82].strip()
					x_accl = line [82:94].strip()
					y_accl = line [94:106].strip()
					z_accl = line [106:118].strip()
					x_coor = line [118:130].strip()
					y_coor = line [130:142].strip()
					z_coor = line [142:154].strip()
					
					node = self.nodout[entity]
					node.x_disp.append (float(x_disp))
					node.y_disp.append (float(y_disp))
					node.z_disp.append (float(z_disp))
					node.x_vel.append (float(x_vel))
					node.y_vel.append (float(y_vel))
					node.z_vel.append (float(z_vel))
					node.x_accl.append (float(x_accl))
					node.y_accl.append (float(y_accl))
					node.z_accl.append (float(z_accl))
					node.x_coor.append (float(x_coor))
					node.y_coor.append (float(y_coor))
					node.z_coor.append (float(z_coor))
					
					line = file.readline()

				line = file.readline()
				line = file.readline()
				line = file.readline()
				line = file.readline()
				line = file.readline()
				line = file.readline()
				while line:
					entity = line [0:10].strip()
					if (not self.nodout.has_key (entity) ):
						break
					
					x_rot = line [10:22].strip()
					y_rot = line [22:34].strip()
					z_rot = line [34:46].strip()
					x_rot_vel = line [46:58].strip()
					y_rot_vel = line [58:70].strip()
					z_rot_vel = line [70:82].strip()
					x_rot_accl = line [82:94].strip()
					y_rot_accl = line [94:106].strip()
					z_rot_accl = line [106:118].strip()
					
					node = self.nodout[entity]
					node.x_rot.append (float(x_rot))
					node.y_rot.append (float(y_rot))
					node.z_rot.append (float(z_rot))
					node.x_rot_vel.append (float(x_rot_vel))
					node.y_rot_vel.append (float(y_rot_vel))
					node.z_rot_vel.append (float(z_rot_vel))
					node.x_rot_accl.append (float(x_rot_accl))
					node.y_rot_accl.append (float(y_rot_accl))
					node.z_rot_accl.append (float(z_rot_accl))
					
					line = file.readline()
			
			line = file.readline()
				
				
				