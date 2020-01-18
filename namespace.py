#%% 
# Function Definition
def area_circle(radius):
    pi=22/7
    area=pi*radius**2
    return area

# Main body
radius=10
Area=area_circle(radius)
Circumference=2*Area/radius
print("Area: ", Area, " | Circumference: ", Circumference)
