# -*- coding: cp1251 -*-
#
#	geometry analysis
#

import math

class geometry:
	def __init__ (self):
		pass
	
	@staticmethod
	def plane (p1,p2,p3):
		
		(x1,y1,z1) = p1
		(x2,y2,z2) = p2
		(x3,y3,z3) = p3
		
		A = y1 *(z2 - z3) + y2* (z3 - z1) + y3*(z1 - z2)
		B = z1 *(x2 - x3) + z2* (x3 - x1) + z3*(x1 - x2)
		C = x1 *(y2 - y3) + x2* (y3 - y1) + x3*(y1 - y2)
		D = - (x1*(y2* z3 - y3* z2) + x2 *(y3* z1 - y1* z3) + x3* (y1* z2 - y2* z1))
		
		return (A,B,C,D)
	
	
	
	
	
	@staticmethod
	def distance_Point_Plane (p, pl):
		(xa,ya,za) = p
		(A,B,C,D) = pl
	
		ro=(A*xa + B*ya + C*za + D) / math.sqrt(A*A + B*B + C*C)
		
		
		return ro
	
	@staticmethod	
	def projection_point_plane (p, pl):
		(x,y,z) = p
		(A,B,C,D) = pl
		
		t= (-D-A*x-B*y-C*z)/(A*A + B*B + C*C)
		x2 = x+t*A
		y2 = y+t*B
		z2 = z+t*C
		
		return (x2,y2,z2)
	
	
	
class analysis:

	# расчет расстояния от т.p до треугольника з1бз2бз3 во времени
	@staticmethod
	def history_distance (p, p1, p2, p3):
	
		(xt,yt,zt) = p
		(xt1,yt1,zt1) = p1
		(xt2,yt2,zt2) = p2
		(xt3,yt3,zt3) = p3
		
		rot = []
		
		for x,y,z,x1,y1,z1,x2,y2,z2,x3,y3,z3 in zip (xt,yt,zt,xt1,yt1,zt1, xt2,yt2,zt2,  xt3,yt3,zt3):
			pl = geometry.plane ( (x1,y1,z1), (x2,y2,z2), (x3,y3,z3))
			ro = geometry.distance_Point_Plane ((x,y,z), pl)
			rot.append (ro)
	
		return rot
	
	def run (self):
		self.read_config ("config.txt")
		self.read_nodout ("nodout")
		self.hdd = self.history_analysis()
		self.write ("graphics.txt")
		
	
	def read_config (self, config_name):
	
		file = open (config_name, "r")
		self.points = []
		for line in file:
			sl = line.split (" ")
			p = sl[0].strip()
			p1 = sl[1].strip()
			p2 = sl[2].strip()
			p3 = sl[3].strip()
			
#			print p,p1,p2,p3
			
			self.points.append ((p,p1,p2,p3))
		
		
	def read_nodout (self, nodout_name):
	
		import reader
		r=reader.lsdyna_reader ()
		r.read_nodout ('nodout')
		
		self.nodout = r.nodout
		
		
	def history_analysis (self):	
		
		time = self.nodout['__time']
		hdd = dict ()
		hdd ['time'] = time
		for i in self.points:
			(ep, ep1,ep2,ep3) = i
#			print ep
			sp = self.nodout [ep]
			sp1 = self.nodout [ep1]
			sp2 = self.nodout [ep2]
			sp3 = self.nodout [ep3]
			p = (sp.x_coor, sp.y_coor, sp.z_coor)
			p1 = (sp1.x_coor, sp1.y_coor, sp1.z_coor)
			p2 = (sp2.x_coor, sp2.y_coor, sp2.z_coor)
			p3 = (sp3.x_coor, sp3.y_coor, sp3.z_coor)
			
			hd = analysis.history_distance (p, p1, p2, p3)
			hdd [sp.title] = hd
			
		return hdd

	def write (self, file_name):
	
		file = open (file_name, "w")
		
		line = ''
#		for entity, value  in self.hdd.iteritems():
#			line = ';'.join ([line,  entity])
		
		line = ';'.join ([ entity       for entity, value  in self.hdd.iteritems()])
		line+='\n'
		file.write( line )
		n = len (self.hdd['time'])
		
		for i in xrange (n):
			line = ''
#			for entity, value  in self.hdd.iteritems():
#				line = ';'.join ([line,  str(value[i])])
			line = ';'.join ([str(value[i])       for entity, value  in self.hdd.iteritems()])
			line+='\n'
			file.write( line )
			
			
		
		
		
		
		
		
		
		
		
	
	
	
	
		
		