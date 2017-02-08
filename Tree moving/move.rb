mod = Sketchup.active_model # Open model
ent = mod.entities # All entities in model
sel = mod.selection # Current selection
# east 1
transformation = Geom::Transformation.new([10.m,0,0])
# west 1
#transformation = Geom::Transformation.new([-10.m,0,0])
# north 1
#transformation = Geom::Transformation.new([0,2.m,0])
# south 1
#transformation = Geom::Transformation.new([0,-0.5.m,0])
Sketchup.active_model.entities.transform_entities(transformation,sel)

#instance = sel[0]
#puts instance
