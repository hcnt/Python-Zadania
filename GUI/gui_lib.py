# -*- coding: utf-8 -*-

#PLAN_IX
#(c) Jarosław Bylina, LGPL
#last change ID: 2018-05-23-b

import copy
import datetime
import tkinter as Tkinter

class Window(object):
    _ix_widgets = {
        'L': Tkinter.Label,
        'B': Tkinter.Button,
        'E': Tkinter.Entry,
        'C': Tkinter.Checkbutton,
    }
    _var_needed = {'C'}
    _whole_gui = None
    _windows = {}
    _last_id = 0
    def __init__(self, title, **data):
        if self._whole_gui == None:
            self._whole_gui = Tkinter.Tk()
            self._whole_gui.withdraw()
        self.root = Tkinter.Toplevel(self._whole_gui)
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.root.title(title)
        self.cont = {}
        self.rows = []
        self.defaults = data  ##_ix_make_colors(data)
        self.last_row = 0
        self.images = {}
        self.vars = object()
        self._inner_vars = {}
        self._last_id += 1
        self.my_id = self._last_id
        self._windows[self.my_id] = self.root
    def _ix_expand_array(self, arr, ind, stuff):
        while ind >=len (arr):
            arr.append(stuff)
    def _conf_com(self, widget, name, row, col, command):
        if command!=None:
            widget.config(command=(lambda:command(app=self, name=name, row=row, col=col)))
    def _conf_im(self, widget, image):
        if image!=None:
            if image not in self.images:
                self.images[image] = Tkinter.PhotoImage(file=image)
##                self.images[image] = PIL.ImageTk.PhotoImage(PIL.Image.open(image))
            widget.config(image=self.images[image])
    def add(self, what, row=None, col=None, rowspan=1, colspan=1, name=None, image=None, command=None, **data):
        aux_data = copy.deepcopy(self.defaults)
##        aux_data.update(_ix_make_colors(data))
        aux_data.update(data)
        if name in self.cont:
            raise KeyError('The name "%s" exists in this application already...' % (name,))
        if row == None:
            row = self.last_row
        self.last_row = row
        self._ix_expand_array(self.rows, row, -1)
        if col == None:
            col = self.rows[row]+1
        self.rows[row] = max(col, self.rows[row])
        if what in self._var_needed:
            aux_data['variable'] = self._inner_vars[name] = Tkinter.IntVar()
        widget = self._ix_widgets[what](self.root, aux_data)
        widget.grid(row=row, rowspan=rowspan, column=col, columnspan=colspan)
        if name!=None:
            self.cont[name] = widget
        self.cont[(row, col)] = widget
        self._conf_im(widget, image)
        self._conf_com(widget, name, row, col, command)
    def start(self, *dummy1, **dummy2):
        #self.root.mainloop()
        self._whole_gui.wait_window(self.root)
    def hide(self, *dummy1, **dummy2):
        self.root.withdraw()
    def close(self, *dummy1, **dummy2):
        #self.root.quit()
        self.root.withdraw()
        self.root.destroy()
        del self._windows[self.my_id]
    def config(self, name=None, row=None, col=None, image=None, command=None, **data):
        if name==None:
            name = (row, col)
        elif row==None and col==None:
            pass  # name = name
        elif row==None:
            name = (name, col)
        else:  # if col==None:
            name = (name, row)
        self._conf_im(self.cont[name], image)
        self._conf_com(self.cont[name], name, None, None, command)
        self.cont[name].config(**data)
    def getC(self, name):
        return bool(self._inner_vars[name].get())
    def togC(self, name):
        self.cont[name].toggle()
    def setC(self, name, value):
        if value:
            self.cont[name].select()
        else:
            self.cont[name].deselect()
    def getE(self, name):
        return self.cont[name].get()
    def setE(self, name, value):
        self.cont[name].delete(0, Tkinter.END)
        self.cont[name].insert(0, value)


##def Array(*dims, **stuff_def):
##    stuffing = stuff_def.get("stuffing")
##    for dim in dims[::-1]:
##        stuffing = [copy.deepcopy(stuffing) for i in range(dim)]
##    return stuffing


##class Timer(object):
##    def start(self):
##        self.T = datetime.datetime.now()
##        print "[START]"
##    def time(self):
##        print "[LAP TIME]: ", datetime.datetime.now() - self.T


##class Record(object):
##    def __init__(self, *flist, **fdict):
##        for n in flist:
##            object.__setattr__(self, n, None)
##        for (n, v) in fdict.items():
##            object.__setattr__(self, n, v)
##    def __delattr__(self, n):
##        raise AttributeError("Cannot delete fields in Record.")
##    def __setattr__(self, n, v):
##        if n in self.__dict__:
##            object.__setattr__(self, n, v)
##        else:
##            raise AttributeError("Cannot create new fields in Record.")
##    def __repr__(self):
##        return "Record(%s)" % (", ".join(
##            ["%s=%s" % (n, repr(v))
##                for (n, v) in self.__dict__.items()]
##        ),)
##    def __lt__(self, other):
##        raise TypeError("Cannot order Records.")
##    def __gt__(self, other):
##        raise TypeError("Cannot order Records.")
##    def __le__(self, other):
##        raise TypeError("Cannot order Records.")
##    def __ge__(self, other):
##        raise TypeError("Cannot order Records.")
##    def __eq__(self, other):
##        if isinstance(other, Record):
##            return self.__dict__==other.__dict__
##        else:
##            raise TypeError("Cannot compare Record with anything of different type.")
##    def __ne__(self, other):
##        return not self==other


##def Image(path):
##    import PIL.Image
##    im = PIL.Image.open(path)
##    im.load()
##    ws, hs = im.size
##    result = Array(hs, ws)
##    pixels = list(im.getdata())
##    i = 0
##    for h in range(hs):
##        for w in range(ws):
##            result[h][w] = Record(r=pixels[i][0],
##                                     g=pixels[i][1],
##                                     b=pixels[i][2],
##                                     a=pixels[i][3])
##            i += 1
##    print im.mode
##    return result


##def ImageSave(arr, path):
##    import PIL.Image
##    im = PIL.Image.new("RGBA", (len(arr[0]), len(arr)))
