#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.7.1 on Fri Mar 10 20:50:38 2017
#

import wx
import entrada as E
#Registro Usuarios
import GuardarUsuario as GU
import BuscarUsuario as BU
import ModificarUsuario as MU
import EliminarUsuario as EU

#Operaciones Usuarios
import BloquearUsuario as BU
import DesbloquearUsuario as DU

#Registro Postulantes
import GuardarPostulante as GP
import BuscarPostulante as BP

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class Principal(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Principal.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE
        wx.Frame.__init__(self, *args, **kwds)
        self.vntPpal_BarraEstado = self.CreateStatusBar(1)
        self.tree = wx.TreeCtrl(self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.TR_DEFAULT_STYLE | wx.TR_HAS_BUTTONS | wx.TR_LINES_AT_ROOT)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("Seleccion de Personal"))
        self.bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("iconos/personal.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/salir1.png", wx.BITMAP_TYPE_ANY))
        self.bitmap_button_2 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("iconos/soporte_tecnico_icono1.png", wx.BITMAP_TYPE_ANY))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        self.Bind(wx.EVT_BUTTON, self.OnSalir, self.bitmap_button_1)
        # end wxGlade
        #LLenar el TreeCtrl
        root = self.tree.AddRoot('Inicio')
        Re = self.tree.AppendItem(root, 'Registros')
        Op=self.tree.AppendItem(root,'Operaciones')
      
        Repor=self.tree.AppendItem(root,'Reportes')
        

        Po = self.tree.AppendItem(Re, 'Postulantes')
        Us=self.tree.AppendItem(Re,'Usuarios')
        Blo=self.tree.AppendItem(Op,'Bloquear Usuarios')
        Des=self.tree.AppendItem(Op,'Desbloquear Usuarios')
        Bi=self.tree.AppendItem(Repor,'Bitacora')
        
        
        self.tree.AppendItem(Po, 'Buscar Postulante')
        
        self.tree.AppendItem(Po, 'Guardar Postulante')
        

        self.tree.AppendItem(Us, 'Buscar Usuario')
        self.tree.AppendItem(Us, 'Eliminar Usuario')
        self.tree.AppendItem(Us, 'Guardar Usuario')
        self.tree.AppendItem(Us, 'Modificar Usuario')
        
        

        self.tree.AppendItem(Bi, 'Bitacora')
        self.tree.AppendItem(Bi, 'Bitacora por Ano')
        self.tree.AppendItem(Bi, 'Bitacora por Mes')
        self.tree.AppendItem(Bi, 'Bitacora por Dia')
        self.tree.AppendItem(Bi, 'Reporte Usuarios')
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED,self.OnSelChanged,id=1)

    def __set_properties(self):
        # begin wxGlade: Principal.__set_properties
        self.SetTitle(_("Principal Administrador"))
        self.SetSize((802, 500))
        self.vntPpal_BarraEstado.SetStatusWidths([-1])
        
        # statusbar fields
        vntPpal_BarraEstado_fields = [_("Listo")]
        for i in range(len(vntPpal_BarraEstado_fields)):
            self.vntPpal_BarraEstado.SetStatusText(vntPpal_BarraEstado_fields[i], i)
        self.tree.SetMinSize((180,100))
        self.label_1.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Cantarell"))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        self.bitmap_button_2.SetSize(self.bitmap_button_2.GetBestSize())
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Principal.__do_layout
        grid_sizer_1 = wx.FlexGridSizer(1, 3, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_3 = wx.FlexGridSizer(1, 2, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(6, 1, 0, 0)
        grid_sizer_1.Add(self.tree, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add(self.bitmap_1, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_4.Add(self.bitmap_button_1, 0, 0, 0)
        grid_sizer_4.Add(self.bitmap_button_2, 0, 0, 0)
        grid_sizer_3.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_3.AddGrowableRow(0)
        grid_sizer_3.AddGrowableCol(0)
        grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_2.AddGrowableRow(1)
        grid_sizer_2.AddGrowableCol(0)
        grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnSelChanged(self, event):  # wxGlade: Principal.<event_handler>
        item =  event.GetItem()
        #new=self.display.SetLabel(self.tree.GetItemText(item))
        if self.tree.GetItemText(item)== "Guardar Usuario":
            Ventana=GU.Principal(self)
            Ventana.Show()
            

        if self.tree.GetItemText(item)== "Buscar Usuario":
            Ventana=BU.Principal(self)
            Ventana.Show()
            

        if self.tree.GetItemText(item)== "Modificar Usuario":
            Ventana=MU.Principal(self)
            Ventana.Show()
            
        if self.tree.GetItemText(item)== "Eliminar Usuario":
            Ventana=EU.Principal(self)
            Ventana.Show()
            

        if self.tree.GetItemText(item)== "Bloquear Usuarios":
            Ventana=BU.Principal(self)
            Ventana.Show()
            

        if self.tree.GetItemText(item)== "Desbloquear Usuarios":
            Ventana=DU.Principal(self)
            Ventana.Show()
           

        if self.tree.GetItemText(item)== "Guardar Postulante":
            Ventana=GP.Principal(self)
            Ventana.Show()
            

        if self.tree.GetItemText(item)== "Buscar Postulante":
            Ventana=BP.Principal(self)
            Ventana.Show()
            

    def EnSalir(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            Ventana=E.Principal(self)
            Ventana.Show()
            self.Hide()
        dlg.Destroy()

    def OnInfoSys(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnInfoSys' not implemented!"
        event.Skip()

    def OnContact(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnContact' not implemented!"
        event.Skip()

    def OnManual(self, event):  # wxGlade: Principal.<event_handler>
        print "Event handler 'OnManual' not implemented!"
        event.Skip()

    def OnSalir(self, event):  # wxGlade: Principal.<event_handler>
        dlg = wx.MessageDialog(None, '¿Desea Salir?',
                           'Dialogo de Mensage', wx.OK|wx.CANCEL|
                            wx.ICON_QUESTION)
        #dlg.ShowModal()
        

        if dlg.ShowModal()==wx.ID_OK:
            Ventana=E.Principal(self)
            Ventana.Show()
            self.Hide()
        dlg.Destroy()
# end of class Principal

if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.App()
    #wx.InitAllImageHandlers()
    frame_1 = Principal(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()