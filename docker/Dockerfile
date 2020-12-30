FROM centos
COPY logger.py /home
COPY my_logger.service /etc/systemd/system
RUN yum install -y python3
RUN systemctl enable my_logger
CMD ["/sbin/init"]
