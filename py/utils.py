"""
# 0
import pcbnew
pcbnew.GetBoard().SetGridOrigin(pcbnew.wxPointMM(0,0))
pcbnew.Refresh()
"""


"""
# キースイッチ
import pcbnew
pcbnew.GetBoard().SetGridOrigin(pcbnew.wxPointMM(95.25,63.5))
pcbnew.Refresh()
"""

"""
# ユニバーサル 1.27間隔用のグリッド
import pcbnew
pcbnew.GetBoard().SetGridOrigin(pcbnew.wxPointMM(0,0))
pcbnew.Refresh()
"""

"""
# 外形用 0.5mm grid
import pcbnew
pcbnew.GetBoard().SetGridOrigin(pcbnew.wxPointMM(75.775,43.6125))
pcbnew.Refresh()
"""

"""
# トラックボール用
import pcbnew
pcbnew.GetBoard().SetGridOrigin(pcbnew.wxPointMM(264.025,117.475))
pcbnew.Refresh()
"""

