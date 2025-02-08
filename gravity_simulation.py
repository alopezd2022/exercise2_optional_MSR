import pybullet as p
import pybullet_data
import time
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,0)

# Create the plane with its collision
plane_collision_id = p.createCollisionShape(shapeType=p.GEOM_PLANE)
plane_id = p.createMultiBody(baseCollisionShapeIndex=plane_collision_id)

# Create the sphere with its collision
sphere_collision_id = p.createCollisionShape(shapeType=p.GEOM_SPHERE, radius=0.5)
sphere_id = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=sphere_collision_id, basePosition=[0.0,0.0,3.0])

# Initial data
y0 = 3.0
v0 = 0.0
a = -9.81
y = y0
v = v0
t = 1/20

while (1):
    
    if p.getContactPoints(sphere_id, plane_id):
        v = 0
        y = 0.5
    else :
        v = v + a * t
        y = y0 + v * t + (1/2) * a * t**2

    # Change the position of the sphere in eacht iteration
    p.resetBasePositionAndOrientation(bodyUniqueId=sphere_id, posObj=[0.0,0.0,y], ornObj=[0,0,0,1])


    p.stepSimulation()
    time.sleep(t)
    
p.disconnect()