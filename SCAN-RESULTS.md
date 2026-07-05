# Baseline Vulnerability Scan Results

Generated: 2026-07-05
Scanner: OWASP Dependency-Check v12.1.0
Total Vulnerabilities (CVSS >= 7.0): 150

---

[INFO] Scanning for projects...
[INFO] 
[INFO] -----------------------< com.veracode:verademo >------------------------
[INFO] Building verademo 0.0.1-SNAPSHOT
[INFO]   from pom.xml
[INFO] --------------------------------[ war ]---------------------------------
[INFO] 
[INFO] --- dependency-check:12.1.0:check (default-cli) @ verademo ---
[INFO] Checking for updates
[INFO] Skipping the NVD API Update as it was completed within the last 240 minutes
[INFO] Skipping Known Exploited Vulnerabilities update check since last check was within 24 hours.
[INFO] Check for updates complete (488 ms)
[INFO] 

Dependency-Check is an open source tool performing a best effort analysis of 3rd party dependencies; false positives and false negatives may exist in the analysis performed by the tool. Use of the tool and the reporting provided constitutes acceptance for use in an AS IS condition, and there are NO warranties, implied or otherwise, with regard to the analysis or its use. Any use of the tool and the reporting provided is at the user's risk. In no event shall the copyright holder or OWASP be held liable for any damages whatsoever arising out of or in connection with the use of this tool, the analysis performed, or the resulting report.


   About ODC: https://jeremylong.github.io/DependencyCheck/general/internals.html
   False Positives: https://jeremylong.github.io/DependencyCheck/general/suppression.html

💖 Sponsor: https://github.com/sponsors/jeremylong


[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (0 seconds)
[INFO] Finished CPE Analyzer (1 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[INFO] Finished RetireJS Analyzer (0 seconds)
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot-starter-web/2.3.1.RELEASE/spring-boot-starter-web-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/fasterxml/jackson/core/jackson-annotations/2.11.0/jackson-annotations-2.11.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/fasterxml/jackson/core/jackson-databind/2.11.0/jackson-databind-2.11.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot-starter-json/2.3.1.RELEASE/spring-boot-starter-json-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/yaml/snakeyaml/1.26/snakeyaml-1.26.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-jcl/5.2.7.RELEASE/spring-jcl-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-core/5.2.7.RELEASE/spring-core-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/slf4j/jul-to-slf4j/1.7.30/jul-to-slf4j-1.7.30.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/logging/log4j/log4j-api/2.13.3/log4j-api-2.13.3.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/logging/log4j/log4j-to-slf4j/2.13.3/log4j-to-slf4j-2.13.3.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/ch/qos/logback/logback-core/1.2.3/logback-core-1.2.3.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/ch/qos/logback/logback-classic/1.2.3/logback-classic-1.2.3.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot-starter-logging/2.3.1.RELEASE/spring-boot-starter-logging-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot-starter/2.3.1.RELEASE/spring-boot-starter-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/felix/org.osgi.core/1.2.0/org.osgi.core-1.2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/sling/maven-sling-plugin/2.0.4-incubator/maven-sling-plugin-2.0.4-incubator.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-expression/5.2.7.RELEASE/spring-expression-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-context/5.2.7.RELEASE/spring-context-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-aop/5.2.7.RELEASE/spring-aop-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-webmvc/5.2.7.RELEASE/spring-webmvc-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-beans/5.2.7.RELEASE/spring-beans-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/spring-web/5.2.7.RELEASE/spring-web-5.2.7.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/fasterxml/jackson/module/jackson-module-parameter-names/2.11.0/jackson-module-parameter-names-2.11.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.11.0/jackson-datatype-jsr310-2.11.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/fasterxml/jackson/datatype/jackson-datatype-jdk8/2.11.0/jackson-datatype-jdk8-2.11.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.11.0/jackson-core-2.11.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/wagon/wagon-provider-api/1.0-alpha-5/wagon-provider-api-1.0-alpha-5.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-repository-metadata/2.0/maven-repository-metadata-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-artifact-manager/2.0/maven-artifact-manager-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-model/2.0/maven-model-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-profile/2.0/maven-profile-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-project/2.0/maven-project-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-archiver/2.0/maven-archiver-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-plugin-api/2.0/maven-plugin-api-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/sling/org.apache.sling.api/2.0.2-incubator/org.apache.sling.api-2.0.2-incubator.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/sling/org.apache.sling.commons.osgi/2.0.2-incubator/org.apache.sling.commons.osgi-2.0.2-incubator.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/sling/org.apache.sling.commons.json/2.0.4-incubator/org.apache.sling.commons.json-2.0.4-incubator.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/commons-codec/commons-codec/1.14/commons-codec-1.14.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/mysql/mysql-connector-java/5.1.48/mysql-connector-java-5.1.48.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/santuario/xmlsec/1.5.1/xmlsec-1.5.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/keycloak/keycloak-saml-core/1.8.1.Final/keycloak-saml-core-1.8.1.Final.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/com/veracode/annotation/VeracodeAnnotations/1.2.1/VeracodeAnnotations-1.2.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/maven/maven-artifact/2.0/maven-artifact-2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/classworlds/classworlds/1.1-alpha-2/classworlds-1.1-alpha-2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/codehaus/plexus/plexus-archiver/1.0-alpha-3/plexus-archiver-1.0-alpha-3.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/hamcrest/hamcrest/2.2/hamcrest-2.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/hamcrest/hamcrest-core/2.2/hamcrest-core-2.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/junit/junit/4.13/junit-4.13.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/codehaus/plexus/plexus-container-default/1.0-alpha-8/plexus-container-default-1.0-alpha-8.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/codehaus/plexus/plexus-utils/1.0.4/plexus-utils-1.0.4.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot/2.3.1.RELEASE/spring-boot-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot-devtools/2.3.1.RELEASE/spring-boot-devtools-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/owasp/encoder/encoder/1.2.2/encoder-1.2.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/mindrot/jbcrypt/0.3m/jbcrypt-0.3m.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/apache/commons/commons-collections4/4.0/commons-collections4-4.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/log4j/log4j/1.2.17/log4j-1.2.17.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/slf4j/slf4j-log4j12/1.7.7/slf4j-log4j12-1.7.7.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/javax/xml/bind/jaxb-api/2.3.1/jaxb-api-2.3.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/commons-fileupload/commons-fileupload/1.3.2/commons-fileupload-1.3.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/owasp/encoder/encoder-jsp/1.2.2/encoder-jsp-1.2.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/jakarta/annotation/jakarta.annotation-api/1.3.5/jakarta.annotation-api-1.3.5.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/var/folders/sz/0k46jj5x13j45ln_6pntmtd00000gp/T/dctemp6c35f6dd-35be-432d-b8c8-2030332b2a5b/check15311949548103437261tmp/65/org/springframework/boot/devtools/livereload/livereload.js' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/Documents/github/veracode-wad26/verademo-java/app/src/main/webapp/resources/js/jquery-1.11.2.min.js' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/Documents/github/veracode-wad26/verademo-java/app/src/main/webapp/resources/js/bootstrap.min.js' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/Documents/github/veracode-wad26/verademo-java/app/src/main/webapp/resources/js/bootstrap.js' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/Documents/github/veracode-wad26/verademo-java/app/src/main/webapp/resources/js/npm.js' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/javax/activation/activation/1.1/activation-1.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/javax/mail/mail/1.4.7/mail-1.4.7.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/Users/bbaukema/.m2/repository/org/springframework/boot/spring-boot-autoconfigure/2.3.1.RELEASE/spring-boot-autoconfigure-2.3.1.RELEASE.jar' (Sonatype OSS Index Analyzer).
[INFO] Finished Sonatype OSS Index Analyzer (12 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (14 seconds)
[INFO] Writing HTML report to: /Users/bbaukema/Documents/github/veracode-wad26/verademo-java/app/target/dependency-check-report.html
[WARNING] 

One or more dependencies were identified with known vulnerabilities in verademo:

VeracodeAnnotations-1.2.1.jar (pkg:maven/com.veracode.annotation/VeracodeAnnotations@1.2.1, cpe:2.3:a:veracode:veracode:1.2.1:*:*:*:*:*:*:*) : CVE-2023-25721, CVE-2023-25722
bootstrap.js (pkg:javascript/bootstrap@3.3.2) : CVE-2016-10735, CVE-2018-14040, CVE-2018-14042, CVE-2018-20676, CVE-2018-20677, CVE-2019-8331, CVE-2024-6485, Bootstrap before 4.0.0 is end-of-life and no longer maintained.
bootstrap.min.js (pkg:javascript/bootstrap@3.3.2) : CVE-2016-10735, CVE-2018-14040, CVE-2018-14042, CVE-2018-20676, CVE-2018-20677, CVE-2019-8331, CVE-2024-6485, Bootstrap before 4.0.0 is end-of-life and no longer maintained.
commons-collections4-4.0.jar (pkg:maven/org.apache.commons/commons-collections4@4.0, cpe:2.3:a:apache:commons_collections:4.0:*:*:*:*:*:*:*) : CVE-2015-6420
commons-fileupload-1.3.2.jar (pkg:maven/commons-fileupload/commons-fileupload@1.3.2, cpe:2.3:a:apache:commons_fileupload:1.3.2:*:*:*:*:*:*:*) : CVE-2016-1000031, CVE-2023-24998, CVE-2025-48976
commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*) : CVE-2012-5783, CVE-2020-13956
commons-io-2.4.jar (pkg:maven/commons-io/commons-io@2.4, cpe:2.3:a:apache:commons_io:2.4:*:*:*:*:*:*:*) : CVE-2021-29425, CVE-2024-47554
jackson-databind-2.11.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.11.0, cpe:2.3:a:fasterxml:jackson-core:2.11.0:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-databind:2.11.0:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.11.0:*:*:*:*:*:*:*) : CVE-2026-54512, CVE-2026-54513, CVE-2020-36518, CVE-2021-46877, CVE-2022-42003, CVE-2022-42004, CVE-2026-50193, CVE-2026-54514, CVE-2026-54515, CVE-2023-35116
jbcrypt-0.3m.jar (pkg:maven/org.mindrot/jbcrypt@0.3m, cpe:2.3:a:mindrot:jbcrypt:0.3m:*:*:*:*:*:*:*) : CVE-2015-0886
jquery-1.11.2.min.js (pkg:javascript/jquery@1.11.2.min) : CVE-2015-9251, CVE-2019-11358, CVE-2020-11023, jquery issue: 11974, jquery issue: 162
junit-4.13.jar (pkg:maven/junit/junit@4.13, cpe:2.3:a:junit:junit4:4.13:*:*:*:*:*:*:*) : CVE-2020-15250
keycloak-saml-core-1.8.1.Final.jar (pkg:maven/org.keycloak/keycloak-saml-core@1.8.1.Final, cpe:2.3:a:keycloak:keycloak:1.8.1:*:*:*:*:*:*:*, cpe:2.3:a:redhat:keycloak:1.8.1:*:*:*:*:*:*:*) : CVE-2022-1245, CVE-2021-20195, CVE-2019-14837, CVE-2017-12161, CVE-2019-10199, CVE-2020-1714, CVE-2020-1718, CVE-2023-6787, CVE-2016-8609, CVE-2018-14637, CVE-2019-10201, CVE-2020-14389, CVE-2023-6563, CVE-2017-2646, CVE-2019-14832, CVE-2020-10758, CVE-2020-14366, CVE-2021-3513, CVE-2021-3632, CVE-2021-3637, CVE-2021-20202, CVE-2019-10169, CVE-2019-10170, CVE-2023-6291, CVE-2024-7341, CVE-2021-3827, CVE-2022-3916, CVE-2016-8629, CVE-2017-2582, CVE-2020-27838, CVE-2022-1466, CVE-2024-4629, CVE-2021-20323, CVE-2022-4361, CVE-2024-7260, CVE-2017-2585, CVE-2020-1758, CVE-2020-1744, CVE-2019-10157, CVE-2020-1698, CVE-2020-1697, CVE-2020-1725, CVE-2020-1727, CVE-2020-1728, CVE-2022-1274, CVE-2023-6134, CVE-2020-10770, CVE-2023-0264, CVE-2018-10912, CVE-2020-14302, CVE-2020-1694, CVE-2026-0871, CVE-2019-3875, CVE-2020-10776, CVE-2019-14820, CVE-2020-1724, CVE-2021-3856, CVE-2020-27826, CVE-2019-3868
log4j-1.2.17.jar (pkg:maven/log4j/log4j@1.2.17, cpe:2.3:a:apache:log4j:1.2.17:*:*:*:*:*:*:*) : CVE-2019-17571, CVE-2020-9493, CVE-2022-23305, CVE-2022-23302, CVE-2022-23307, CVE-2023-26464
log4j-api-2.13.3.jar (pkg:maven/org.apache.logging.log4j/log4j-api@2.13.3, cpe:2.3:a:apache:log4j:2.13.3:*:*:*:*:*:*:*) : CVE-2026-34479, CVE-2026-34480, CVE-2025-68161, CVE-2026-34477
logback-core-1.2.3.jar (pkg:maven/ch.qos.logback/logback-core@1.2.3, cpe:2.3:a:qos:logback:1.2.3:*:*:*:*:*:*:*) : CVE-2023-6378, CVE-2021-42550
maven-sling-plugin-2.0.4-incubator.jar (pkg:maven/org.apache.sling/maven-sling-plugin@2.0.4-incubator, cpe:2.3:a:apache:sling:2.0.4:*:*:*:*:*:*:*) : CVE-2016-0956, CVE-2013-4390
mysql-connector-java-5.1.48.jar (pkg:maven/mysql/mysql-connector-java@5.1.48, cpe:2.3:a:oracle:mysql_connector\/j:5.1.48:*:*:*:*:*:*:*) : CVE-2023-22102, CVE-2019-2692, CVE-2020-2934, CVE-2020-2875, CVE-2020-2933
org.apache.sling.api-2.0.2-incubator.jar (pkg:maven/org.apache.sling/org.apache.sling.api@2.0.2-incubator, cpe:2.3:a:apache:sling:2.0.2:*:*:*:*:*:*:*, cpe:2.3:a:apache:sling_api:2.0.2:*:*:*:*:*:*:*) : CVE-2022-32549, CVE-2015-2944
org.apache.sling.commons.json-2.0.4-incubator.jar (pkg:maven/org.apache.sling/org.apache.sling.commons.json@2.0.4-incubator, cpe:2.3:a:apache:sling:2.0.4:*:*:*:*:*:*:*, cpe:2.3:a:apache:sling_commons_json:2.0.4:*:*:*:*:*:*:*) : CVE-2022-47937
plexus-archiver-1.0-alpha-3.jar (pkg:maven/org.codehaus.plexus/plexus-archiver@1.0-alpha-3, cpe:2.3:a:codehaus-plexus:plexus-archiver:1.0:pha-3:*:*:*:*:*:*) : CVE-2023-37460, CVE-2018-1002200
plexus-utils-1.0.4.jar (pkg:maven/org.codehaus.plexus/plexus-utils@1.0.4, cpe:2.3:a:codehaus-plexus:plexus-utils:1.0.4:*:*:*:*:*:*:*, cpe:2.3:a:utils_project:utils:1.0.4:*:*:*:*:*:*:*) : CVE-2017-1000487, CVE-2025-67030, CVE-2022-4244, CVE-2022-4245
snakeyaml-1.26.jar (pkg:maven/org.yaml/snakeyaml@1.26, cpe:2.3:a:snakeyaml_project:snakeyaml:1.26:*:*:*:*:*:*:*) : CVE-2022-1471, CVE-2022-25857, CVE-2022-38749, CVE-2022-38751, CVE-2022-38752, CVE-2022-41854, CVE-2022-38750
spring-boot-2.3.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot@2.3.1.RELEASE, cpe:2.3:a:vmware:spring_boot:2.3.1:release:*:*:*:*:*:*) : CVE-2023-20873, CVE-2026-22733, CVE-2023-20883, CVE-2026-40972, CVE-2026-40975, CVE-2026-40973, CVE-2026-40977
spring-boot-devtools-2.3.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot-devtools@2.3.1.RELEASE, cpe:2.3:a:vmware:spring_boot:2.3.1:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_boot_tools:2.3.1:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_tools:2.3.1:release:*:*:*:*:*:*) : CVE-2023-20873, CVE-2026-22733, CVE-2023-20883, CVE-2026-40972, CVE-2026-40975, CVE-2026-40973, CVE-2026-40977
spring-boot-starter-web-2.3.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot-starter-web@2.3.1.RELEASE, cpe:2.3:a:vmware:spring_boot:2.3.1:release:*:*:*:*:*:*, cpe:2.3:a:web_project:web:2.3.1:release:*:*:*:*:*:*) : CVE-2023-20873, CVE-2026-22733, CVE-2023-20883, CVE-2026-40972, CVE-2026-40975, CVE-2026-40973, CVE-2026-40977
spring-core-5.2.7.RELEASE.jar (pkg:maven/org.springframework/spring-core@5.2.7.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_framework:5.2.7:release:*:*:*:*:*:*) : CVE-2022-22965, CVE-2024-22259, CVE-2021-22118, CVE-2020-5421, CVE-2022-22950, CVE-2022-22971, CVE-2023-20861, CVE-2023-20863, CVE-2026-22740, CVE-2026-22737, CVE-2022-22968, CVE-2022-22970, CVE-2026-22745, CVE-2021-22060, CVE-2021-22096, CVE-2026-22741, CVE-2026-22735
spring-web-5.2.7.RELEASE.jar (pkg:maven/org.springframework/spring-web@5.2.7.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:web_project:web:5.2.7:release:*:*:*:*:*:*) : CVE-2016-1000027, CVE-2022-22965, CVE-2024-22259, CVE-2021-22118, CVE-2020-5421, CVE-2022-22950, CVE-2022-22971, CVE-2023-20861, CVE-2023-20863, CVE-2026-22740, CVE-2026-22737, CVE-2022-22968, CVE-2022-22970, CVE-2026-22745, CVE-2021-22060, CVE-2021-22096, CVE-2026-22741, CVE-2026-22735
spring-webmvc-5.2.7.RELEASE.jar (pkg:maven/org.springframework/spring-webmvc@5.2.7.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:web_project:web:5.2.7:release:*:*:*:*:*:*) : CVE-2022-22965, CVE-2024-22259, CVE-2021-22118, CVE-2020-5421, CVE-2022-22950, CVE-2022-22971, CVE-2023-20861, CVE-2023-20863, CVE-2026-22740, CVE-2026-22737, CVE-2022-22968, CVE-2022-22970, CVE-2026-22745, CVE-2021-22060, CVE-2021-22096, CVE-2026-22741, CVE-2026-22735
xmlsec-1.5.1.jar (pkg:maven/org.apache.santuario/xmlsec@1.5.1, cpe:2.3:a:apache:santuario_xml_security_for_java:1.5.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:xml_security_for_java:1.5.1:*:*:*:*:*:*:*) : CVE-2021-40690, CVE-2023-44483, CVE-2013-2172, CVE-2013-4517


See the dependency-check report for more details.


[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  16.287 s
[INFO] Finished at: 2026-07-03T23:37:20+02:00
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.owasp:dependency-check-maven:12.1.0:check (default-cli) on project verademo: 
[ERROR] 
[ERROR] One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '7.0': 
[ERROR] 
[ERROR] commons-collections4-4.0.jar (pkg:maven/org.apache.commons/commons-collections4@4.0, cpe:2.3:a:apache:commons_collections:4.0:*:*:*:*:*:*:*): CVE-2015-6420(9.8)
[ERROR] commons-fileupload-1.3.2.jar (pkg:maven/commons-fileupload/commons-fileupload@1.3.2, cpe:2.3:a:apache:commons_fileupload:1.3.2:*:*:*:*:*:*:*): CVE-2023-24998(7.5), CVE-2016-1000031(9.8), CVE-2025-48976(7.5)
[ERROR] jackson-databind-2.11.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.11.0, cpe:2.3:a:fasterxml:jackson-core:2.11.0:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-databind:2.11.0:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.11.0:*:*:*:*:*:*:*): CVE-2021-46877(7.5), CVE-2026-50193(6.3), CVE-2020-36518(7.5), CVE-2026-54512(8.1), CVE-2026-54513(8.1), CVE-2022-42003(7.5), CVE-2022-42004(7.5)
[ERROR] keycloak-saml-core-1.8.1.Final.jar (pkg:maven/org.keycloak/keycloak-saml-core@1.8.1.Final, cpe:2.3:a:keycloak:keycloak:1.8.1:*:*:*:*:*:*:*, cpe:2.3:a:redhat:keycloak:1.8.1:*:*:*:*:*:*:*): CVE-2019-10199(8.8), CVE-2019-14832(7.5), CVE-2019-14837(9.1), CVE-2021-3632(7.5), CVE-2021-3637(7.5), CVE-2021-3513(7.5), CVE-2017-2646(7.5), CVE-2019-10201(8.1), CVE-2023-6787(8.8), CVE-2019-10169(7.2), CVE-2022-1245(9.8), CVE-2020-14389(8.1), CVE-2019-10170(7.2), CVE-2021-20202(7.3), CVE-2023-6291(7.1), CVE-2016-8609(8.1), CVE-2018-14637(8.1), CVE-2024-7341(7.1), CVE-2023-6563(7.7), CVE-2020-10758(7.5), CVE-2021-20195(9.6), CVE-2017-12161(8.8), CVE-2020-1718(8.8), CVE-2020-1714(8.8), CVE-2020-14366(7.5)
[ERROR] log4j-1.2.17.jar (pkg:maven/log4j/log4j@1.2.17, cpe:2.3:a:apache:log4j:1.2.17:*:*:*:*:*:*:*): CVE-2020-9493(9.8), CVE-2022-23307(8.8), CVE-2022-23305(9.8), CVE-2023-26464(7.5), CVE-2019-17571(9.8), CVE-2022-23302(8.8)
[ERROR] log4j-api-2.13.3.jar (pkg:maven/org.apache.logging.log4j/log4j-api@2.13.3, cpe:2.3:a:apache:log4j:2.13.3:*:*:*:*:*:*:*): CVE-2026-34480(6.9), CVE-2026-34479(6.9)
[ERROR] logback-core-1.2.3.jar (pkg:maven/ch.qos.logback/logback-core@1.2.3, cpe:2.3:a:qos:logback:1.2.3:*:*:*:*:*:*:*): CVE-2023-6378(7.5), CVE-2021-42550(6.6)
[ERROR] maven-sling-plugin-2.0.4-incubator.jar (pkg:maven/org.apache.sling/maven-sling-plugin@2.0.4-incubator, cpe:2.3:a:apache:sling:2.0.4:*:*:*:*:*:*:*): CVE-2016-0956(7.5)
[ERROR] mysql-connector-java-5.1.48.jar (pkg:maven/mysql/mysql-connector-java@5.1.48, cpe:2.3:a:oracle:mysql_connector\/j:5.1.48:*:*:*:*:*:*:*): CVE-2023-22102(8.3)
[ERROR] org.apache.sling.commons.json-2.0.4-incubator.jar (pkg:maven/org.apache.sling/org.apache.sling.commons.json@2.0.4-incubator, cpe:2.3:a:apache:sling:2.0.4:*:*:*:*:*:*:*, cpe:2.3:a:apache:sling_commons_json:2.0.4:*:*:*:*:*:*:*): CVE-2022-47937(9.8)
[ERROR] plexus-archiver-1.0-alpha-3.jar (pkg:maven/org.codehaus.plexus/plexus-archiver@1.0-alpha-3, cpe:2.3:a:codehaus-plexus:plexus-archiver:1.0:pha-3:*:*:*:*:*:*): CVE-2023-37460(9.8)
[ERROR] plexus-utils-1.0.4.jar (pkg:maven/org.codehaus.plexus/plexus-utils@1.0.4, cpe:2.3:a:codehaus-plexus:plexus-utils:1.0.4:*:*:*:*:*:*:*, cpe:2.3:a:utils_project:utils:1.0.4:*:*:*:*:*:*:*): CVE-2017-1000487(9.8), CVE-2025-67030(8.8), CVE-2022-4244(7.5)
[ERROR] snakeyaml-1.26.jar (pkg:maven/org.yaml/snakeyaml@1.26, cpe:2.3:a:snakeyaml_project:snakeyaml:1.26:*:*:*:*:*:*:*): CVE-2022-25857(7.5), CVE-2022-1471(9.8)
[ERROR] spring-boot-2.3.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot@2.3.1.RELEASE, cpe:2.3:a:vmware:spring_boot:2.3.1:release:*:*:*:*:*:*): CVE-2023-20873(9.8), CVE-2023-20883(7.5), CVE-2026-40972(7.5), CVE-2026-40975(7.5), CVE-2026-22733(8.1), CVE-2026-40973(7.0)
[ERROR] spring-boot-devtools-2.3.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot-devtools@2.3.1.RELEASE, cpe:2.3:a:vmware:spring_boot:2.3.1:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_boot_tools:2.3.1:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_tools:2.3.1:release:*:*:*:*:*:*): CVE-2023-20873(9.8), CVE-2023-20883(7.5), CVE-2026-40972(7.5), CVE-2026-40975(7.5), CVE-2026-22733(8.1), CVE-2026-40973(7.0)
[ERROR] spring-boot-starter-web-2.3.1.RELEASE.jar (pkg:maven/org.springframework.boot/spring-boot-starter-web@2.3.1.RELEASE, cpe:2.3:a:vmware:spring_boot:2.3.1:release:*:*:*:*:*:*, cpe:2.3:a:web_project:web:2.3.1:release:*:*:*:*:*:*): CVE-2023-20873(9.8), CVE-2023-20883(7.5), CVE-2026-40972(7.5), CVE-2026-40975(7.5), CVE-2026-22733(8.1), CVE-2026-40973(7.0)
[ERROR] spring-core-5.2.7.RELEASE.jar (pkg:maven/org.springframework/spring-core@5.2.7.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_framework:5.2.7:release:*:*:*:*:*:*): CVE-2024-22259(8.1), CVE-2022-22965(9.8), CVE-2021-22118(7.8)
[ERROR] spring-web-5.2.7.RELEASE.jar (pkg:maven/org.springframework/spring-web@5.2.7.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:web_project:web:5.2.7:release:*:*:*:*:*:*): CVE-2024-22259(8.1), CVE-2016-1000027(9.8), CVE-2022-22965(9.8), CVE-2021-22118(7.8)
[ERROR] spring-webmvc-5.2.7.RELEASE.jar (pkg:maven/org.springframework/spring-webmvc@5.2.7.RELEASE, cpe:2.3:a:pivotal_software:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:springsource:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:vmware:spring_framework:5.2.7:release:*:*:*:*:*:*, cpe:2.3:a:web_project:web:5.2.7:release:*:*:*:*:*:*): CVE-2024-22259(8.1), CVE-2022-22965(9.8), CVE-2021-22118(7.8)
[ERROR] xmlsec-1.5.1.jar (pkg:maven/org.apache.santuario/xmlsec@1.5.1, cpe:2.3:a:apache:santuario_xml_security_for_java:1.5.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:xml_security_for_java:1.5.1:*:*:*:*:*:*:*): CVE-2021-40690(7.5)
[ERROR] 
[ERROR] See the dependency-check report for more details.
[ERROR] 
[ERROR] 
[ERROR] -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
