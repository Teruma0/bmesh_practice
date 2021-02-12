# -*- encoding:utf-8 -*-

import bpy
import math
import random
import os
import bmesh

def all_activate():
    for all in bpy.data.objects:
        bpy.context.view_layer.objects.active = all

def all_select():
    for all in bpy.data.objects:
        all.select_set(True)

def all_deselect():
    for all in bpy.data.objects:
        all.select_set(False)

def all_delete():
    for i in bpy.data.objects:
        bpy.data.objects.remove(i)
    for i in bpy.data.meshes:
        bpy.data.meshes.remove(i)
    for i in bpy.data.collections:
        bpy.data.collections.remove(i)

all_delete()

obj_path = bpy.path.abspath('/Users/wakabayashiteruma/Desktop/room.obj')
bpy.ops.import_scene.obj(filepath = obj_path)
ceiling = bpy.data.objects["textured_output.001"]
ceiling.hide_viewport = True

active = bpy.context.object.data
bm = bmesh.new()
bm.from_mesh(active)
"""
for obj in bpy.data.objects:
        if obj.name.startswith('Cube'):
            bpy.context.view_layer.objects.active = obj
"""
for v in range():
    list(bm.verts)[i].select_set(True)
    x = list(bm.verts)[i].co.x
    y = list(bm.verts)[i].co.y
    z = list(bm.verts)[i].co.z
    if  z >= 1.5:
        list(bm.verts)[i].co.z +=5
        bm.to_mesh(active)
    else:
        bm.to_mesh(active)
    return

bm.free()
