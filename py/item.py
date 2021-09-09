import pcbnew
import math


#PITCH = float(2.38125 * 4)
PITCH = float(2.54)
OFFSET_X = 0
OFFSET_Y = 0
o = 0
REF_NAME_PRE = 'JUC_B'
BEGIN_NUM = 53
END_NUM = 56

COL_COUNT = 1

pcb = pcbnew.GetBoard()

# グリッドの原点の設定(ど真ん中)
#pcb.SetGridOrigin(pcbnew.wxPointMM(OFFSET_X+PITCH*2,OFFSET_Y+PITCH*2))


def sin(deg):
	return math.sin(math.radians(deg))

def cos(deg):
	return math.cos(math.radians(deg))

def set_position_keyswitch(ref):
	module = pcb.FindModuleByReference(REF_NAME_PRE+str(ref))
	if module is not None:
		ref = ref - 1
		module.SetPosition(pcbnew.wxPointMM((int(ref)%COL_COUNT) * PITCH + OFFSET_X, (int(ref)//COL_COUNT) * PITCH + OFFSET_Y))
		module.SetOrientation( o * 10.0 )


def set_position(ref, xp, yp, o = 0):
	module = pcb.FindModuleByReference(ref)
	if module is not None:
		module.SetPosition(pcbnew.wxPointMM(xp, yp))

for ref in range(BEGIN_NUM,END_NUM):
	set_position_keyswitch(ref)


pcbnew.Refresh() #Refreshで画面には反映されるが、編集したことにはならないので、保存するにはひと工夫必要
