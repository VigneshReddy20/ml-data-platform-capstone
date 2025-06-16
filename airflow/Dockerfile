FROM apache/airflow:2.8.1-python3.10

USER root

RUN apt-get update && apt-get install -y iputils-ping

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Install Java 17 and curl, then install Spark 3.5.1
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless curl && \
    curl -L https://archive.apache.org/dist/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz | \
    tar -xz -C /opt && \
    ln -s /opt/spark-3.5.1-bin-hadoop3 /opt/spark && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_HOME=/opt/spark
ENV PATH="${SPARK_HOME}/bin:$PATH"

USER airflow

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
