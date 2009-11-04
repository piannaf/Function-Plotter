



###################################################################
#
#   CSSE1001 - Assignment 2
#
#   Student Number:
#
#   Student Name:
#
###################################################################


#
# Do not change the following import
#

from assign2_support import *

####################################################################
#
# Insert your code below
#
####################################################################

import tkColorChooser

class World_Screen:
    """ Map between world and screen coordinates

    Precondition: Floating point arguments are assumed for initialization
    of every World_Screen object.

    Constructor: World_Screen(xmin, ymin, xmax, ymax, width, height)
    """
    def __init__(self, xmin=0, ymin=0, xmax=0, ymax=0, width=0, height=0):
        self._xmin, self._ymin = xmin, ymin
        self._xmax, self._ymax = xmax, ymax
        self._width, self._height = width, height

    def world2screen(self, x, y):
        """ Map the coordinates x, y in the world's domain to the coordinates
        xc, yc in the screen's domain.

        This function accepts both float and integer arguments. Float arguments
        are indicated below as Python will automatically cast an int to float
        when necessary.

        world2screen(float, float) -> (float, float)
        """
        self.xc = (x - self._xmin)*self._width/(self._xmax - self._xmin)
        self.yc = (self._height) - \
            (y - self._ymin)*(self._height)/(self._ymax - self._ymin)

        return (self.xc, self.yc)

    def screen2world(self, xc, yc):
        """ Map the coordinates xc, yc in the screen's domain to the coordinates
        x, y in the world's domain.

        This function accepts both float and integer arguments. Float arguments
        are indicated below as Python will automatically cast an int to float
        when necessary.

        screen2world(float, float) -> (float, float)
        """
        self._x = xc*(self._xmax - self._xmin)/self._width + self._xmin
        self._y = (self._height - yc)* \
            (self._ymax - self._ymin)/self._height + self._ymin

        return (self._x, self._y)

class FunctionFrame(Frame):
    """ Contains widgets for entering a function definition and choosing
    the plot colour for the function.

    Constructor: FunctionFrame(master)
    """
    def __init__(self, master):
        Frame.__init__(self, master, bd = 1, relief = SUNKEN, pady = 5,
                       bg = '#dddddd')

        # construct the function entry widget
        self._func = ''
        Label(self, text = 'Function in x: ', bg = '#dddddd').pack(side = LEFT)
        self._funcEntry = Entry(self, width = 50)
        self._funcEntry.pack(side = LEFT)

        # construct the colour choosing widget
        self._chosenColor = "black"
        self._selectButton = Button(self, text = 'Select',
                                    command = self.selectColour,
                                    takefocus = FALSE)
        self._selectButton.pack(side = RIGHT, padx = 5)
        self._colourEntry = Entry(self, width = 20)
        self._colourEntry.insert(END, self._chosenColor)
        self._colourEntry.pack(side = RIGHT)
        Label(self, text = 'Function Colour: ', bg = '#dddddd').pack(side = RIGHT)

    def selectColour(self):
        """ Creates a popup for the tkColorChooser widget and returns the
        chosen colour

        selectColour(void) -> string
        """
        self._chosenColor = tkColorChooser.askcolor(self.getColor(),
                                                    title = "Choose a Colour")
        if self._chosenColor[1]:
            self._colourEntry.delete(0, END)
            
            # tkColorChooser returns a pair
            # the second entry is a string representing 8bit hex
            self._chosenColor = self._chosenColor[1]
            self._colourEntry.insert(END, self._chosenColor)
            

    def getColor(self):
        """ Getter method which returns the chosen color

        getColor(void) -> string
        """
        return self._colourEntry.get()

    def getFunction(self):
        """ Checks whether the input function is valid.
        If the function is valid, it will be returned.
        If the function is not valid, None will be returned.

        getFunc(void) -> function OR None
        """
        self._func = self._funcEntry.get()
        if self._func == '':
            raise myFunctionError("'' is not a valid function")
        try:
            return make_function(self._funcEntry.get()) 
        except FunctionError:
            raise myFunctionError("'%s' is not a valid function" % self._func)

        return None

class PlotFrame(Frame):
    """ Contains widgets for entering plot information.

    Constructor: PlotFrame(master)
    """
    def __init__(self, master):
        Frame.__init__(self, master, bd = 1, relief = SUNKEN, pady = 5,
                       bg = '#dddddd')

        Label(self, text = 'Plot Settings', bg = '#dddddd',
              width = 12, anchor = W).pack(side = LEFT)
        
        Label(self, text = 'Start X: ', bg = '#dddddd',
              width = 8, anchor = E).pack(side = LEFT)
        self._startxEntry = Entry(self, width = 10)
        self._startxEntry.pack(side = LEFT)
        
        Label(self, text = 'End X: ', bg = '#dddddd',
              width = 8, anchor = E).pack(side = LEFT)
        self._endxEntry = Entry(self, width = 10)
        self._endxEntry.pack(side = LEFT)
        
        Label(self, text = 'Start Y: ', bg = '#dddddd',
              width = 8, anchor = E).pack(side = LEFT)
        self._startyEntry = Entry(self, width = 10)
        self._startyEntry.pack(side = LEFT)
        
        Label(self, text = 'End Y: ', bg = '#dddddd',
              width = 8, anchor = E).pack(side = LEFT)
        self._endyEntry = Entry(self, width = 10)
        self._endyEntry.pack(side = LEFT)
        
        Label(self, text = 'Steps: ', bg = '#dddddd',
              width = 8, anchor = E).pack(side = LEFT)
        self._stepsEntry = Entry(self, width = 10)
        self._stepsEntry.pack(side = LEFT)

    def getStartx(self):
        """ Getter method which returns startx or raises an error if startx is
        not a real number

        getStartx(void) -> float
        """
        try:
            return float(self._startxEntry.get())
        except:
            raise myFunctionError("Start X must be a real number")

    def getEndx(self):
        """ Getter method which returns endx or raises an error if endx is not
        a real number

        getEndx(void) -> float
        """
        try:
            return float(self._endxEntry.get())
        except:
            raise myFunctionError("End X must be a real number")
        
    def getStarty(self):
        """ Getter method which returns starty or raises an error if starty is
        not a real number

        getStarty(void) -> float
        """
        try:
            return float(self._startyEntry.get())
        except:
            raise myFunctionError("Start Y must be a real number")

    def getEndy(self):
        """ Getter method which returns endy or raises an error if endy is not
        a real number

        getEndy(void) -> float
        """
        try:
            return float(self._endyEntry.get())
        except:
            raise myFunctionError("End Y must be a real number")

    def getSteps(self):
        """ Getter method which returns the number of steps or raises an error
        if the number of steps is not an integer greater than zero

        getSteps(void) -> int
        """
        try:
            steps = int(self._stepsEntry.get())
            if steps > 0:
                return steps
            else:
                raise Exception
        except:
            raise myFunctionError("The number of steps must be a positive integer")
    

    def getPlotInfo(self):
        """ Getter mothod which returns a tuple consisting of all plot
        information available from this class or raises an error if the minimum
        of x is bigger than the maximum of x or if the minimum of y is bigger than
        the maximum of y.

        getPlotInfo(void) -> (starx, starty, endx, endy, steps)
        """
        startx = self.getStartx();
        endx = self.getEndx();
        starty = self.getStarty();
        endy = self.getEndy();
        steps = self.getSteps();
        
        if endx <= startx:
            raise myFunctionError("Start X must be smaller than End X")

        if endy <= starty:
            raise myFunctionError("Start Y must be smaller than End Y")

        return((startx, starty, endx, endy, steps))        

class ButtonFrame(Frame):
    """ Contains widgets for user interaction
    This class defines a custom widget to be used in PlotApp

    Constructor: ButtonFrame(master)
    """
    def __init__(self, master):
        Frame.__init__(self, master, pady = 5)

        self.addFunction = Button(self,
                                  text = 'Add Function', bg = '#eeeeee',
                                  takefocus = FALSE)
        self.addFunction.pack(side = LEFT)
        
        self.redrawAll = Button(self,
                                text = 'Redraw All Functions', bg = '#eeeeee',
                                takefocus = FALSE)
        self.redrawAll.pack(side = LEFT)
        
        self.removeLast = Button(self,
                                 text = 'Remove Last Function', bg = '#eeeeee',
                                 takefocus = FALSE)
        self.removeLast.pack(side = LEFT)
        
        self.removeAll = Button(self,
                                text = 'Remove All Functions', bg = '#eeeeee',
                                takefocus = FALSE)
        self.removeAll.pack(side = LEFT)
        
        self.exitApp = Button(self, text = 'Exit', bg = '#eeeeee',
                              takefocus = FALSE)
        self.exitApp.pack(side = LEFT)

class myFunctionError(FunctionError):
    """ Extends the FunctionError class defined in assign2_support.py by
    creating an error message box containing the error.

    Code for this class is a modification of the python documentation
    section 8.5. User-defined Exceptions.

    Constructor: myFunctionError(string)
    """
    def __init__(self, value):
        self._value = value
        self.showError(self._value)

    def showError(self, value):
        """Show the error message in a tkMessageBox

        showError(string) -> None
        """
        tkMessageBox.showerror("Error", value)
    

class PlotApp:
    """ This class defines the top level application. All widgets are
    initialized into a predefined layout. Methods of this class handle user to
    application interaction as well as widget to widget communication.

    Constructor: PlotApp(master)
    """
    def __init__(self, master):
        # initialize main window
        master.minsize(700,480)
        master.geometry("800x600")
        
        self._master = master
        self._frame = Frame(self._master)
        self._frame.pack(fill = BOTH, expand = 1)
        
        # initialize function and plot store
        self._allFunctions = []
        self._plotInfo = ()

        # initialize layout
        ## Create a status bar to record mouse events
        self._statusFrame = Frame(self._frame)
        self._statusFrame.pack(side = TOP, fill = X)
        
        self._LPCString = StringVar()
        self._LPCString.set("Last Point Clicked: None")
        self._statusBarLPC = Label(self._statusFrame,
                                   textvariable = self._LPCString)
        self._statusBarLPC.pack(side = LEFT)

        self._PosString = StringVar()
        self._PosString.set("Cursor Point: None")
        self._statusBarPos = Label(self._statusFrame,
                                   textvariable = self._PosString)
        self._statusBarPos.pack(side = LEFT, padx = 10)
        
        ## Create the plot canvas
        self._canvasBD = 2
        self._canvas = Canvas(self._frame,
                              bg = 'white', bd = self._canvasBD,
                              relief = SUNKEN)
        self._canvas.pack(side = TOP, fill = BOTH, expand = 1,
                          pady = 5, padx = 5)
                
        ## initialize world as congruent to screen
        ## because the canvas has a thick border, alter width and height
        self._ws = World_Screen(0, 0,
                                self._canvas.winfo_width(),
                                self._canvas.winfo_height(),
                                self._canvas.winfo_width()-self._canvasBD,
                                self._canvas.winfo_height()-2*self._canvasBD)

        ## Create canvas bindings
        self._canvas.bind('<Button-1>', lambda e: self._LPCString.set(
            'Last Point Clicked: (%.2f, %.2f)\t' %
                self._ws.screen2world(float(e.x), float(e.y))))
        self._canvas.bind('<Motion>', lambda e: self._PosString.set(
            'Cursor Point: (%.2f, %.2f)\t' %
                self._ws.screen2world(float(e.x), float(e.y))))
        self._canvas.bind("<Configure>", lambda e: self.redrawAll())

        ## Place all other widgets
        self._widgetHolder = Frame(self._frame)
        self._widgetHolder.pack(side = BOTTOM, fill = X)
        
        self._funcFrame = FunctionFrame(self._widgetHolder)
        self._funcFrame.pack(side = TOP, fill = X, pady = 10)
        
        self._plotFrame = PlotFrame(self._widgetHolder)
        self._plotFrame.pack(side = TOP, fill = X, pady = 10)

        self._buttonFrame = ButtonFrame(self._widgetHolder)
        self._buttonFrame.pack(side = TOP, pady = 5)
        
        # set up interaction
        self._buttonFrame.addFunction.config(command = self.addFunction)
        self._buttonFrame.redrawAll.config(command = self.redrawAll)
        self._buttonFrame.removeLast.config(command = self.removeLast)
        self._buttonFrame.removeAll.config(command = self.removeAllFunctions)
        self._buttonFrame.exitApp.config(command = self.exitApp)
        
    def addFunction(self):
        """ Appends a valid function to the function list and draws it onto
        the canvas with the appropriate parameters
        """

        # Create a dictionary to store information about the function
        function = {}
        function['f'] = self._funcFrame.getFunction()
        function['color'] = self._funcFrame.getColor()

        # store the newly defined plot information
        self._plotInfo = self._plotFrame.getPlotInfo()

        # Add new function information to the function list
        self._allFunctions.append(function)

        # Redraw everything unless there's nothing currently
        self.drawPlot(self._allFunctions[-1], self._plotInfo)
        self.redrawAll()
            

    def redrawAll(self):
        """ Redraws all functions in the function list """
        self.removeAllPlots()

        # set plot information to current unless this is the initial canvas
        if self._plotInfo:
            self._plotInfo = self._plotFrame.getPlotInfo()
        
        for function in self._allFunctions:
            self.drawPlot(function, self._plotInfo)

    def removeLast(self):
        try:
            self._canvas.delete(self._allFunctions.pop(-1)['canvasObj'])
        except:
            raise myFunctionError(
                "You must add a function before you can remove it.")

    def removeAllFunctions(self):
        """ Removes all functions from the function list"""
        self.removeAllPlots()
        self._allFunctions = []
        
    def removeAllPlots(self):
        """ Removes all plots currently drawn on the canvas"""
        for function in self._allFunctions:
            self._canvas.delete(function['canvasObj'])

    def drawPlot(self, function, plotInfo):
        """ Plots a function onto the canvas given a valid function and plotInfo
        tuple consisting of (startx, starty, endx, endy, steps). The plot will
        be coloured according to colour.
        """        
        f = function['f']
        minx, miny, maxx, maxy, steps = plotInfo
        color = function['color']

        # canvas has a thick border, alter width and height        
        # this still doesn't solve the problem completely
        self._ws = World_Screen(minx, miny, maxx, maxy,
                          self._canvas.winfo_width() - self._canvasBD,
                          self._canvas.winfo_height() - 2*self._canvasBD)

        #calculate the set of x values we will input into the function based
        #on the number of steps given
        rangeX = [(step*maxx - (step - steps)*minx)/steps for step in range(steps + 1)]
        try:
            coords = [self._ws.world2screen(x, f(x)) for x in rangeX]
        except ZeroDivisionError:
            rangeX.remove(0)
            coords = [self._ws.world2screen(x, f(x)) for x in rangeX]
        except ValueError:
            #This get's called for fractional powers with negative bases
            try:
                #if steps is even this will be fast at finding 0
                #and removing everything before it
                rangeX = rangeX[rangeX.index(0):]
                coords = [self._ws.world2screen(x, f(x)) for x in rangeX]
            except:
                #find the first occurance of a positive number
                i = 0
                for x in rangeX:
                    if x < 0:
                        i += 1
                rangeX = rangeX[i:]
                coords = [self._ws.world2screen(x, f(x)) for x in rangeX]

        try:
            function['canvasObj'] = self._canvas.create_line(coords,
                                                             fill = color)
        except TclError:
            raise myFunctionError("Invalid Color")
    def exitApp(self):
        self._master.destroy()

####################################################################
#
# WARNING: Leave the following code at the end of your code
#
# DO NOT CHANGE ANYTHING BELOW
#
####################################################################

def main():
    root = Tk()
    app = PlotApp(root)
    root.mainloop()

if  __name__ == '__main__':
    main()
