#! /bin/sh
sphinx-build -a -b latex src pdf
(cd pdf; make)
cp pdf/IntroductiontoProfessionalWebDevelopmentinJavaScript.pdf intro-to-web-dev.pdf
