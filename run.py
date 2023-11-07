from main import app

if __name__ == "__main__":
    from main.main import controller
    from main import Base, engine
    Base.metadata.create_all(bind=engine)
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)