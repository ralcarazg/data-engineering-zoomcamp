services:
    postgres:
        image: postgres:13
        environment:
            POSTGRES_USER: airflow
            POSTGRES_PASSWORD: airflow
            POSTGRES_DB: airflow
        volumes:
            - postgres_data:/var/lib/postgresql/data
        healthcheck:
            test: ["CMD-SHELL", "pg_isready -U airflow"]
            interval: 10s
            timeout: 5s
            retries: 5
            restart: always


