with open("README.txt", "w") as f:
    f.write("API ENDPOINTS\n\n")

    f.write("GET /getAll\n")
    f.write("GET /getSingleProduct/{id}\n")
    f.write("POST /addNew\n")
    f.write("DELETE /deleteOne/{id}\n")
    f.write("GET /startsWith/{letter}\n")
    f.write("GET /paginate?start=&end=\n")
    f.write("GET /convert/{id}\n\n")

    f.write("FASTAPI DOCS:\n")
    f.write("http://localhost:8000/docs\n")

print("README.txt generated!")