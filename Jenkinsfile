pipeline {
    agent none
    options {
        skipDefaultCheckout(true)
    }
    environment {
        ALLURE_ENDPOINT = 'https://testing.qameta.in'
        ALLURE_PROJECT_ID = '276'
        ALLURE_RESULTS = 'allure-results'
        TESTS_SUCCESS = "always"
        ALLURECTL_RELEASE = "2.24.0"
        PYTHON_THREADS = "2"
        ALLURE_GIT_FLOW = "true"
    }
    stages {
        stage('Matrix Test') {
            matrix {
                agent {
                    label "${TESTS_OS}"
                }
                axes {
                    axis {
                        name 'TESTS_BROWSER'
                        values 'vivaldi'
                    }
                    axis {
                        name 'TESTS_OS'
                        values 'alfa'
                    }
                }
                stages {
                    stage('checkout') {
                        steps {
                            checkout scm
                        }
                    }
                    stage('get allurectl') {
                        steps {
                            sh """
                            ARCH=\$(uname -m)
                            if [ "\$ARCH" = "aarch64" ]; then
                                ALLURECTL_ARCH="allurectl_linux_arm64"
                            else
                                ALLURECTL_ARCH="allurectl_linux_amd64"
                            fi
                            curl -L -o ./allurectl https://github.com/cheshi-mantu/allurectl-local-builds/releases/download/${params.ALLURECTL_RELEASE}/\$ALLURECTL_ARCH
                            chmod +x ./allurectl
                            """
                            script {
                                env.ALLURECTL_VERSION = sh(script: "./allurectl --version | awk '{print \$NF}'", returnStdout: true).trim()
                            }
                        }
                    }
                    stage('python deps') {
                        steps {
                            sh 'python3 -m pip install --user --break-system-packages --upgrade pytest pytest-xdist allure-pytest'
                        }
                    }
                    stage('Running tests') {
                        steps {
                            script {
                                if (env.TESTS_OS != 'alfa') {
                                    sleep 3
                                }
                            }
                            withEnv([
                                "ALLURE_LAUNCH_NAME=${params.TESTS_TYPE}: ${env.JOB_NAME} - #${env.BUILD_NUMBER}",
                                "ALLURE_LAUNCH_TAGS=allurectl, ${params.TESTS_TYPE}, ${params.TESTS_SUCCESS}, ${params.JENKINS_AGENT}, ${env.BRANCH_NAME}, keep"
                            ]) {
                                withCredentials([string(credentialsId: 'egorivanov_at_testing', variable: 'ALLURE_TOKEN')]) {
                                    sh '''
                                    ./allurectl watch -- pytest tests/poco -n ${PYTHON_THREADS} || true
                                    '''
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}