# 📘 Project Setup: PostgreSQL + pgAdmin with Docker

## 🚀 Running PostgreSQL Database and pgAdmin

### 📦 1. Start PostgreSQL container

```bash
docker run --name <db_container_name> \
  -e POSTGRES_USER=<db_user> \
  -e POSTGRES_PASSWORD=<db_password> \
  -e POSTGRES_DB=<db_name> \
  -p 5433:5432 \
  -d postgres
```

### 2. Start pgAdmin container

```bash
    docker run --name pgadmin \
     -p 5050:80 \
    -e PGADMIN_DEFAULT_EMAIL=admin@example.com \
    -e PGADMIN_DEFAULT_PASSWORD=admin_pass \
    -d dpage/pgadmin4
```

### 3. Access pgAdmin

http://localhost:5050/

### 4. Connect pgAdmin to PostgreSQL

Host name/address: host.docker.internal
Port: 5433
Username: <db_user>
Password: <db_password>
Database: <db_name>
