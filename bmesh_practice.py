# -*- encoding:utf-8 -*-
import bpy
import bmesh
import random

def select_all():
    for all in bpy.data.objects:
        all.select_set(True)

def deselect_all():
    for all in bpy.data.objects:
        all.select_set(False)

def activate_all():
    for all in bpy.data.objects:
        bpy.context.view_layer.objects.active = all

def delete_all():
    for i in bpy.data.objects:
        bpy.data.objects.remove(i)
    for i in bpy.data.meshes:
        bpy.data.meshes.remove(i)
    for i in bpy.data.collections:
        bpy.data.collections.remove(i)

delete_all()

def add_solid(num,x,y):
    for sld in range(num):
        rand_x = random.uniform(1,x/2)
        rand_y = random.uniform(1,y/2)
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        active = bpy.context.object
        active.location.x = random.uniform(-1.5*x,1.5*x)
        active.location.y = random.uniform(-1.5*y,1.5*y)
        active.location.z += rand_x
        active.scale=(rand_x,rand_y,rand_x)
    return

num_cube = 5

add_solid(num_cube,10,10)
select_all()
bpy.ops.object.join()

active = bpy.context.object
active.name ='buildings'
bm = bmesh.new()
bm.from_mesh(active.data)

for i in range(num_cube*8):
    list(bm.verts)[i].select_set(True)
    z = list(bm.verts)[i].co.z
    if  z >= 1:
        list(bm.verts)[i].co.z += random.uniform(1,10)
    bm.to_mesh(active.data)

deselect_all()
bm.free()
