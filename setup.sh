mv cve202135042/urls.py .
mv cve202135042/settings.py .
sudo docker-compose run web django-admin startproject cve202135042 .
mv -f urls.py cve202135042/
mv -f settings.py cve202135042/
