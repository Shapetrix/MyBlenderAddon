import bpy
from bpy import context

#Get the current scene
scene = context.scene

#Get the 3D cursor location
cursor = scene.cursor.location

#Get the active object (assume we have one)
obj = context.active_object

#Use a fixed value for now, eventually make this user adjustable
total = 10

#Add 'total' objects into the scene
for i in range(total):
    #Now make a copy of the object
    obj_new = obj.copy()
    #The new object has to be added to a collection in the scene
    scene.collection.objects.link(obj_new)

    #Now place the object in between the cursor
    #and the active object based on 'i'
    factor = i / total
    #Now we can place the object
    obj_new.location = (obj.location * factor) + (cursor * (1.0 - factor))
