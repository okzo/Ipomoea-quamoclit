import pcbnew
import math

width = 1


# pointsの形のlayersのポリゴンを作る
def insert_keepout_polygon(wx_points, layers=None):

	layers_LSET = pcbnew.LSET()
	if layers is None:
		layers_LSET.AddLayer(pcbnew.F_Cu)
		layers_LSET.AddLayer(pcbnew.B_Cu)
		layers = [pcbnew.F_Cu]
	else:
		for layer in layers:
			layers_LSET.AddLayer(layer)
		
	board = pcbnew.GetBoard()
	area = board.InsertArea(-1, 0xffff, layers[0], 0, 0, pcbnew.ZONE_CONTAINER.DIAGONAL_FULL)
	area.SetLayerSet(layers_LSET)
	area.SetIsKeepout(True)
	area.SetDoNotAllowTracks(True)
	area.SetDoNotAllowVias(True)
	area.SetDoNotAllowCopperPour(True)
	outline = area.Outline()
	outline.RemoveAllContours()
		
	for p in wx_points:
		area.AppendCorner(p, -1)
		#print(p)
		
	if hasattr(area, "BuildFilledSolidAreasPolygons"):
		area.BuildFilledSolidAreasPolygons(board)

	if hasattr(area, "Hatch"):
		area.Hatch()

#centerに指定した位置にradiusの大きさの円をcornersに指定したポリゴン数のlayersで作成する
def insert_keepout_circle(center, radius, corners=16, layers=None):
	points = list()
	center_x = center[0]
	center_y = center[1]

	cos, sin, floor = math.cos, math.sin, math.floor
		
	thi = 0
	dthi = 2 * math.pi / corners
		
	for i in range(corners):
		x = int(floor(center_x + radius * cos(thi)))
		y = int(floor(center_y + radius * sin(thi)))
		points.append(pcbnew.wxPoint(x, y))
		thi += dthi
	
	insert_keepout_polygon(points)


def iter_drawings_from_layer(board, layer, classes):
	for d in board.GetDrawings():
		if d.GetLayer() == layer and isinstance(d, classes):
			yield d
	for m in pcbnew.GetBoard().GetModules():
		for d in m.GraphicalItems():
			if d.GetLayer() == layer and isinstance(d, classes):
				yield d

def create_keepout_line(d,width):
	width = width / 2
	insert_keepout_circle(d.GetStart(), width,16,[pcbnew.F_Cu,pcbnew.B_Cu])
	insert_keepout_circle(d.GetEnd(), width,16,[pcbnew.F_Cu,pcbnew.B_Cu])

	start = d.GetStart()
	end = d.GetEnd()
	rad = math.atan2(end.y-start.y,end.x-start.x) + math.pi / 2
	start1 = pcbnew.wxPoint(start.x + math.cos(rad) *  width, start.y + math.sin(rad) *  width)
	start2 = pcbnew.wxPoint(start.x + math.cos(rad) * -width, start.y + math.sin(rad) * -width)
	end1 = pcbnew.wxPoint(end.x + math.cos(rad) *  width, end.y + math.sin(rad) *  width)
	end2 = pcbnew.wxPoint(end.x + math.cos(rad) * -width, end.y + math.sin(rad) * -width)

	insert_keepout_polygon([
		start1,
		end1,
		end2,
		start2,
	])

def create_keepout_sphere(d,width):
	insert_keepout_circle(d.GetCenter(), d.GetRadius() + width,64,[pcbnew.F_Cu,pcbnew.B_Cu])


# Edge.Cutsの線に対して、widthの幅のkeepoutを生成する
for d in iter_drawings_from_layer(pcbnew.GetBoard(), pcbnew.Edge_Cuts, pcbnew.DRAWSEGMENT):
	if d.GetShape() == 0:
		create_keepout_line(d,pcbnew.FromMM(width))
	elif d.GetShape() == 3: # 円.
		create_keepout_sphere(d,pcbnew.FromMM(width))

# Marginの円と線に対して線(直径)の幅のkeepoutを生成する
for d in iter_drawings_from_layer(pcbnew.GetBoard(), pcbnew.Margin, pcbnew.DRAWSEGMENT):
	if d.GetShape() == 0:
		create_keepout_line(d,d.GetWidth())
	elif d.GetShape() == 2: # 円弧. 
		create_keepout_sphere(d)
	elif d.GetShape() == 3: # 円.
		create_keepout_sphere(d,d.GetWidth() / 2)



"""
insert_keepout_circle(pcbnew.wxPoint(2,0), 3,16,[pcbnew.F_Cu])
insert_keepout_circle(0, 0, 3)
insert_keepout_circle(0, 10, 3,16,[pcbnew.F_Cu])
insert_keepout_circle(0, 20, 3,16,[pcbnew.B_Cu])
insert_keepout_circle(0, 30, 3,16,[pcbnew.F_Cu,pcbnew.B_Cu])

insert_keepout_polygon([
	pcbnew.wxPointMM(0,0),
	pcbnew.wxPointMM(2,0),
	pcbnew.wxPointMM(2,2),
	pcbnew.wxPointMM(0,2),
])

"""

pcbnew.Refresh() #Refreshで画面には反映されるが、編集したことにはならないので、保存するにはひと工夫必要
pcbnew.GetBoard().Save(pcbnew.GetBoard().GetFileName()) #上書き保存する

