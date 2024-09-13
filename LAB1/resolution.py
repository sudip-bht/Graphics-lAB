import glfw

def showResoultion():
    if not glfw.init():
        return
    monitor=glfw.get_primary_monitor()
    vidmode =glfw.get_video_mode(monitor)
    print('Resoultion',vidmode.size.width,'*',vidmode.size.height)
    
if __name__=='__main__':
    showResoultion()

