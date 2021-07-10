FROM ubuntu/nginx

ENV WORKDIR ./

WORKDIR ${WORKDIR}

COPY ./files/sysctl.conf ./etc

COPY ./files/ngx_http_header_filter_module.c ./src/http/

COPY ./files/nginx.conf ./etc/nginx

# COPY ./files/se-ngix_1_0_10.tar.gz ./opt

# RUN tar -zxvf ./opt/se-ngix_1_0_10.tar.gz -C ./opt

# RUN apt update

# RUN apt install policycoreutils selinux-utils selinux-basics -y

# RUN selinux-activate

# RUN apt install make

# RUN cd ./opt/se-ngix_1_0_10/nginx && make
