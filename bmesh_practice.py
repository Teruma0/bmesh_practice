# -*- encoding:utf-8 -*-

import bpy
import bmesh
import random


def all_select():
    for all in bpy.data.objects:
        all.select_set(True)

def deselect_all():
    for all in bpy.data.objects:
        all.select_set(False)

def all_activate():
    for all in bpy.data.objects:
        bpy.context.view_layer.objects.active = all

def all_delete():
    for i in bpy.data.objects:
        bpy.data.objects.remove(i)
    for i in bpy.data.meshes:
        bpy.data.meshes.remove(i)
    for i in bpy.data.collections:
        bpy.data.collections.remove(i)

all_delete()

def add_solid(num,x,y):
    bpy.ops.mesh.primitive_plane_add(location=(0,0,0))
    active = bpy.context.object
    active.scale=(x*1.5,y*1.5,0.1)
    for sld in range(num):
        rand_x = random.uniform(1,x/2)
        rand_y = random.uniform(1,y/2)
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        active = bpy.context.object
        active.location.x = random.uniform(-x,x)
        active.location.y = random.uniform(-y,y)
        active.location.z += rand_x
        active.scale=(rand_x,rand_y,rand_x)
    return
num_cube = 5

add_solid(num_cube,10,10)
all_select()
bpy.ops.object.join()

active1 = bpy.context.object.data
bm = bmesh.new()
bm.from_mesh(active1)
"""
for obj in bpy.data.objects:
        if obj.name.startswith('Cube'):
            bpy.context.view_layer.objects.active = obj
"""
#active = bpy.data.objects['Cube.003']


for i in range(num_cube*8):
    list(bm.verts)[i].select_set(True)
    x = list(bm.verts)[i].co.x
    y = list(bm.verts)[i].co.y
    z = list(bm.verts)[i].co.z
    if  z >= 1:
        list(bm.verts)[i].co.z += random.uniform(1,10)
    bm.to_mesh(active1)

deselect_all()
bm.free()
