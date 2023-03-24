<template>
    <div style="width: 40%; margin: auto">
        <h1 style="margin-top: 30px; margin-bottom: 50px; font-weight: bold">修改密码</h1>
        <br>
        <br>
        <br>
        <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="原密码" prop="oldPass">
                <el-input v-model="ruleForm.oldPass" autocomplete="off" placeholder="请输入原密码"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
                <el-input type="password" v-model="ruleForm.pass" autocomplete="off" placeholder="请输入新密码"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
                <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"
                          placeholder="请确认新密码"></el-input>
            </el-form-item>
            <el-form-item label="验证码" prop="code" :inline="true">
                <el-input v-model.number="ruleForm.code" autocomplete="off" placeholder="默认手机号获取验证码"
                          style="width: 70%"></el-input>
                <el-button type="primary" style="width: 30%" @click="send_sms">{{ sms_interval }}</el-button>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="checkPassword('ruleForm')">提交</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
            </el-form-item>
            <el-button
                    style="display: none"
                    plain
                    @click="open1">
            </el-button>

        </el-form>
    </div>
</template>

<script>
    // import CPWD from './Header'
    import Util from "../../assets/js/util";

    export default {
        name: "ChangePassword",
        data() {
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入新密码'));
                } else if (value === this.ruleForm.oldPass) {
                    callback(new Error('新密码与原密码不可相同!'));
                } else {
                    if (this.ruleForm.checkPass !== '') {
                        this.$refs.ruleForm.validateField('checkPass');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.ruleForm.pass) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            var validateCode = (rule, value, callback) => {
                if (!value) {
                    return callback(new Error('验证码不能为空'));
                }
                setTimeout(() => {
                    if (!Number.isInteger(value)) {
                        callback(new Error('请输入数字值'));
                    } else {
                        if (value < 100000 || value > 1000000) {
                            callback(new Error('验证码需要是6位数'));
                        } else {
                            callback();
                        }
                    }
                }, 1000);
            };
            return {
                sms_interval: '获取验证码',
                is_send: false,
                mobile: '',
                checkOldMsg: '',
                error_pass: true,
                ruleForm: {
                    pass: '',
                    checkPass: '',
                    code: '',
                    oldPass: '',
                },
                rules: {
                    pass: [
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {validator: validatePass2, trigger: 'blur'}
                    ],
                    code: [
                        {validator: validateCode, trigger: 'blur'}
                    ],
                }
            };
        },
        methods: {
            send_sms() {
                if (this.is_send) return
                this.is_send = true
                this.$axios.post(`${this.$settings.base_url}get_code/`, {
                    role_id: this.$cookies.get('role_id'),
                    user_id: this.$cookies.get('user_id'),
                }).then(item => {
                    if (item.data.status == 100) {
                        let sms_interval_time = 60;
                        this.sms_interval = "发送中...";
                        let timer = setInterval(() => {
                            if (sms_interval_time <= 1) {
                                clearInterval(timer);
                                this.sms_interval = "获取验证码";
                                this.is_send = false; // 重新回复点击发送功能的条件
                            } else {
                                sms_interval_time -= 1;
                                this.sms_interval = `${sms_interval_time}秒后再发`;
                            }
                        }, 1000);
                        this.mobile = item.data.data
                        console.log(item.data)
                        this.$message({
                            message: item.data.msg,
                            type: 'success',
                            duration: 2000,
                        });
                    } else {
                        this.$message({
                            message: item.data.msg,
                            type: 'error',
                            duration: 2000,
                        });
                    }
                })

            },
            checkPassword(formName) {
                this.$axios.get(`${this.$settings.base_url}check_password/`, {
                    params: {
                        "user_id": this.$cookies.get('user_id'),
                        "old_pass": this.ruleForm.oldPass,
                        "role_id": this.$cookies.get('role_id')
                    }
                }).then(item => {
                    console.log(item)
                    if (item.data.status != 100) {
                        this.checkOldMsg = item.data.data
                        this.open2(this.checkOldMsg)
                    } else {
                        console.log(item.data.status)
                        this.submitForm(formName)
                    }
                }).catch(() => {
                    this.$message({
                        type: 'warning',
                        message: '后端问题!'
                    })
                })
            },
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$axios.post(`${this.$settings.base_url}change_password/`, {
                            role_id: this.$cookies.get('role_id'),
                            user_id: this.$cookies.get('user_id'),
                            password: this.ruleForm.pass,
                            checkpassword: this.ruleForm.checkPass,
                            mobile: this.mobile,
                            code: this.ruleForm.code
                        }).then(response => {
                            if (response.data.status == 100) {
                                let changemsg = response.data.msg
                                this.open1(changemsg)
                                this.open()
                            } else {
                                let errormsg = response.data.msg
                                this.open2(errormsg)
                            }
                        }).catch(() => {
                            this.$message({
                                type: 'warning',
                                message: '后端问题!'
                            })
                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            open1(changemsg) {
                this.$notify({
                    title: '成功',
                    message: changemsg,
                    type: 'success'
                });
            },
            open2(errormsg) {
                this.$notify.error({
                    title: '错误',
                    message: errormsg,
                });
            },
            open() {
                this.$confirm('密码修改成功, 是否立即退出重新登录?', '提示', {
                    confirmButtonText: '退出',
                    cancelButtonText: '稍等一会',
                    type: 'warning'
                }).then(() => {
                    Util.$emit('demo', 'msg');
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消退出'
                    });
                });
            },
        },
        mounted() {

        }
    }
</script>

<style scoped>

</style>