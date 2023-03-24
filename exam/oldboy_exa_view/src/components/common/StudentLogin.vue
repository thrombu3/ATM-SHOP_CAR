<template>
    <div class="login">
        <div class="box">
            <i class="el-icon-close" @click="close_login"></i>
            <div class="content">
                <div class="nav">
                    <p class="text-center">学生登录</p>
                </div>
                <el-form>
                    <el-input
                            placeholder="学号"
                            prefix-icon="el-icon-user"
                            v-model="username"
                            clearable>
                    </el-input>
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-key"
                            v-model="password"
                            clearable
                            show-password>
                    </el-input>
                    <el-button type="primary" @click="login">登录</el-button>
                </el-form>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "StudentLogin",
        data() {
            return {
                username: '',
                password: '',
            }
        },
        methods: {
            close_login() {
                this.$emit('close')
            },
            login() {
                // console.log(this.$settings.base_url);
                if (!(this.username && this.password)) {
                    this.$message({
                        message: '请填入账号和密码',
                        type: 'warning',
                        duration: 1000
                    });
                    return false  // 直接结束函数
                }
                this.$axios.post(this.$settings.base_url + 'login/?type=student', {
                    username: this.username,
                    password: this.password
                }).then(response => {
                    let res = response.data;
                    if (res.status == 100) {
                        let name = res.data.name;
                        let token = res.data.token;
                        let user_id = res.data.user_id;
                        let role_id = res.data.role_id;
                        let role_name = res.data.role_name;
                        this.$cookies.set('name', name, '7d')
                        this.$cookies.set('token', token, '7d')
                        this.$cookies.set('user_id', user_id, '7d')
                        this.$cookies.set('role_id', role_id, '7d')
                        this.$cookies.set('role_name', role_name, '7d')
                        this.$router.push('home')
                        this.$message({
                            message: '登陆成功!',
                            type: 'success',
                        });
                    } else {
                        this.$message({
                            message: res.msg,
                            type: 'warning',
                            duration: 1500,
                            onClose: () => {
                                this.username = '';
                                this.password = ''
                            }
                        })
                    }
                    // 可以捕获接口或处理逻辑出错
                }).catch(error => {
                    this.$message('程序出错,请联系作者');
                    console.log('接口或处理逻辑出错(状态码不是200)');
                    console.log(error)
                })
            },
        }
    }
</script>

<style scoped>
    .login {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 10;
        background-color: rgba(0, 0, 0, 0.3);
    }

    .box {
        width: 400px;
        height: 420px;
        background-color: white;
        border-radius: 10px;
        position: relative;
        top: calc(50vh - 210px);
        left: calc(50vw - 200px);
    }

    .content {
        position: absolute;
        top: 40px;
        width: 280px;
        left: 60px;
    }

    .nav {
        font-size: 20px;
        height: 38px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span {
        margin: 0 20px 0 35px;
        color: darkgrey;
        user-select: none;
        cursor: pointer;
        padding-bottom: 10px;
        border-bottom: 2px solid darkgrey;
    }

    .nav > span.active {
        color: black;
        border-bottom: 3px solid black;
        padding-bottom: 9px;
    }

    .el-input, .el-button {
        margin-top: 40px;
    }

    .el-button {
        width: 100%;
        font-size: 18px;
    }

    .foot > span {
        float: right;
        margin-top: 20px;
        color: orange;
        cursor: pointer;
    }

    .el-icon-close {
        position: absolute;
        font-weight: bold;
        font-size: 20px;
        top: 10px;
        right: 10px;
        cursor: pointer;
    }

</style>