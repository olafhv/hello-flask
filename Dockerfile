FROM harbor.k-space.ee/k-space/microservice-base
ADD hello-world.py /hello-world.py
ENTRYPOINT /hello-world.py
