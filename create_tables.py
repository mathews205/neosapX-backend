import app.db.engine
import app.models
import app.models.base

app.models.base.Base.metadata.create_all(bind=app.db.engine.engine)

print("Tables created successfully.")