<template>
    <div>
        <strong style="float: left;size: 1000px;font-size: 26px; margin-top: 5px; margin-left: 8px; color: #a94442;">老男孩教育</strong>
        <strong style="float: left;size: 1000px;font-size: 20px; margin-top: 8px; margin-left: 20px">考试管理系统</strong>
        <el-drawer
                title="操作须知"
                :visible.sync="drawer1"
                :direction="direction"
                :before-close="handleClose"
                style="font-size: 25px; color: #8d8d8d">
            <p style="font-size: 15px; line-height: 25px">* 请调整您的坐姿, 使面部处于屏幕中央且正对屏幕。</p>
            <p style="font-size: 15px; line-height: 25px">* 按下S键进行拍摄验证。</p>
            <p style="font-size: 15px; line-height: 25px">* 按下ESC键取消拍摄验证。</p>
        </el-drawer>
        <el-drawer
                title="操作须知"
                :visible.sync="drawer2"
                :direction="direction"
                :before-close="handleCloseSign"
                style="font-size: 25px; color: #8d8d8d">
            <p style="font-size: 15px; line-height: 25px">* 请调整您的坐姿, 使面部处于屏幕中央且正对屏幕。</p>
            <p style="font-size: 15px; line-height: 25px">* 按下S键进行拍摄验证。</p>
            <p style="font-size: 15px; line-height: 25px">* 按下ESC键取消拍摄验证。</p>
        </el-drawer>

        <div class="header-avatar">
            <el-badge :value="12" class="item">
                <i class="el-icon-message-solid" style="font-size: 20px;" @click="anno"></i>
            </el-badge>
            <el-avatar size="medium"
                       src="../../assets/img/member1.png"></el-avatar>

            <el-dropdown style="color: aliceblue;;">
						<span class="el-dropdown-link" style="font-weight: bold">
						{{role_name}}: {{name}} <i class="el-icon-arrow-down el-icon--right"></i>
						</span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>
                        <p v-if="sign" @click="sign_in">签到</p>
                        <p v-if="no_sign" @click="sign_in">已签到</p>
                    </el-dropdown-item>
                    <el-dropdown-item><p @click="upLoadNotes">上传笔记</p></el-dropdown-item>
                    <el-dropdown-item><p @click="changePassword">修改密码</p></el-dropdown-item>
                    <el-button
                            style="display: none"
                            plain
                            @click="open1">
                    </el-button>
                    <el-button
                            style="display: none"
                            plain
                            @click="open2">
                    </el-button>
                    <el-button
                            style="display: none"
                            plain
                            @click="open3">
                    </el-button>
                    <el-button
                            style="display: none"
                            @click="drawer = true">
                    </el-button>
                    <el-dropdown-item><p @click="logout">退出</p></el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import Util from "../../assets/js/util";

    export default {
        name: "Header",
        data() {
            return {
                sign: true,
                no_sign: false,
                name: this.$cookies.get('name'),
                user_id: this.$cookies.get('user_id'),
                role_id: this.$cookies.get('role_id'),
                role_name: this.$cookies.get('role_name'),
                infos: '这是考试管理系统的公告!',
                signMsg: '',
                changePasswordMsg: '',
                drawer1: false,
                drawer2: false,
                direction: 'ttb',
            }
        },
        methods: {
            // 校验是否登录
            verify_login() {
                let token = this.$cookies.get('token')
                let role_id = this.$cookies.get('role_id')
                // 主要要校验角色
                if (!token) {
                    this.$message({
                            message: '请先登录',
                            type: 'warning',
                            duration: 1000,
                            onClose: () => {
                                this.$router.push('/')
                            }
                        }
                    );
                    return false
                } else {
                    this.$axios.get(this.$settings.base_url + `verify_login/?role_id=${role_id}`, {
                        headers: {'Authorization': `jwt ${token}`}
                    }).then(response => {
                        // console.log(response.data)
                        if (response.data.status != 100) {
                            this.$message({
                                    message: response.data.msg.detail,
                                    type: 'warning',
                                    duration: 1000,
                                    onClose: () => {
                                        this.$router.push('/')
                                    }
                                }
                            );
                        } else {
                            this.$cookies.set('is_verify', true, '7d')
                        }
                    }).catch(error => {
                        this.$message('程序出错,请联系作者');
                        this.$router.push('/')
                    });
                }
            },
            anno() {
                this.$alert(this.infos, '公告', {
                    confirmButtonText: '确定',
                    callback: action => {
                        this.$message({
                            type: 'info',
                            message: '您可以在头像左侧的消息中心再次查看!'
                        });
                    }
                });
            },
            sign_in() {
                this.$confirm('签到需要进行人脸识别认证, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.drawer2 = true
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消'
                    });
                });

            },
            logout() {
                this.$confirm('是否退出账户?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$cookies.remove('token');
                    this.$cookies.remove('name');
                    this.$cookies.remove('user_id');
                    this.$cookies.remove('role_id');
                    this.$cookies.remove('role_name');
                    this.$cookies.remove('is_verify');
                    this.$message({
                        type: 'success',
                        message: '退出成功!'
                    });
                    this.$router.push('/')
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消退出'
                    });
                });
            },
            changePassword() {
                this.$confirm('修改密码需要进行人脸识别认证, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.drawer1 = true
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消修改'
                    });
                });
            },
            upLoadNotes() {
               this.$router.push('/upload_notes')
            },
            toSign() {
                this.$axios.get(`${this.$settings.base_url}face_compare/`, {
                    params: {val: 1, user_id: this.user_id}
                }).then(response => {
                    if (response.data.status == 100) {
                        this.signMsg = response.data.data_all
                        this.sopen1()
                        this.$axios.get(`${this.$settings.base_url}face_compare/`, {
                            params: {val: 2, user_id: this.user_id}
                        }).then(item => {
                            if (item.data.status == 100) {
                                this.signMsg = item.data.data_all
                                this.sopen1()
                                if (this.sign) {
                                    this.$axios.post(`${this.$settings.base_url}students/get_sign_info/`,
                                        {
                                            id: this.user_id
                                        }).then(item => {
                                        if (item.data.status == 100) {
                                            this.signMsg = '签到成功!'
                                            this.sopen1()
                                            this.sign = false
                                            this.no_sign = true
                                        }
                                    }).catch(() => {
                                        this.$message({
                                            message: '后端错误!'
                                        });
                                    })
                                } else {
                                    this.$message({
                                        type: 'warning',
                                        message: '请勿重复签到!'
                                    });
                                }
                            } else {
                                this.signMsg = item.data.data_all[0]
                                this.sopen2()
                            }
                        }).catch(() =>
                            this.$message({
                                type: 'warning',
                                message: '无法核验您的信息, 请重新拍摄!'
                            })
                        )
                    } else {
                        this.signMsg = response.data.data_all[0]
                        this.sopen3()
                    }
                }).catch(() => {
                    this.$message({
                        type: 'warning',
                        message: '后端问题!'
                    })
                })
            },
            toChange() {
                this.$axios.get(`${this.$settings.base_url}face_compare/`, {
                    params: {val: 1, user_id: this.user_id}
                }).then(response => {
                    if (response.data.status == 100) {
                        this.changePasswordMsg = response.data.data_all
                        this.open1()
                        this.$axios.get(`${this.$settings.base_url}face_compare/`, {
                            params: {val: 2, user_id: this.user_id}
                        }).then(item => {
                            if (item.data.status == 100) {
                                this.changePasswordMsg = item.data.data_all
                                this.open1()
                                this.$router.push('/changepwd')
                            } else {
                                this.changePasswordMsg = item.data.data_all[0]
                                this.open2()
                            }
                        }).catch(() =>
                            this.$message({
                                type: 'warning',
                                message: '无法核验您的信息, 请重新拍摄!'
                            })
                        )
                    } else {
                        this.changePasswordMsg = response.data.data_all[0]
                        this.open3()
                    }
                }).catch(() => {
                    this.$message({
                        type: 'warning',
                        message: '后端问题!'
                    })
                })
            },
            sopen1() {
                this.$notify({
                    title: '成功',
                    message: this.signMsg,
                    type: 'success'
                });
            },
            sopen2() {
                this.$notify.error({
                    title: '错误',
                    message: this.signMsg,
                });
            },
            sopen3() {
                this.$notify({
                    title: '注意',
                    message: this.signMsg,
                    type: 'warning'
                });
            },
            open1() {
                this.$notify({
                    title: '成功',
                    message: this.changePasswordMsg,
                    type: 'success'
                });
            },
            open2() {
                this.$notify.error({
                    title: '错误',
                    message: this.changePasswordMsg,
                });
            },
            open3() {
                this.$notify({
                    title: '注意',
                    message: this.changePasswordMsg,
                    type: 'warning'
                });
            },
            handleClose(done) {
                this.$confirm('确认关闭且前去识别校验？')
                    .then(_ => {
                        done()
                        this.toChange()
                    })
                    .catch(_ => {
                    });
            },
            handleCloseSign(done) {
                this.$confirm('确认关闭且前去识别校验？')
                    .then(_ => {
                        done()
                        this.toSign()
                    })
                    .catch(_ => {
                    });
            }
        },
        created() {
            // 校验是否登录
            let is_verify = this.$cookies.get('is_verify')
            let token = this.$cookies.get('token')
            if (!is_verify) {
                this.verify_login();
                console.log('校验是否登录')
            }

            if (token) {
                this.$axios.get(`${this.$settings.base_url}students/get_sign_info/`,
                    {params: {"id": this.$cookies.get('user_id')}}
                ).then(response => {
                    if (response.data.status == 100) {
                        this.sign = false
                        this.no_sign = true
                    }
                }).catch(() => {
                    this.$message({
                        message: '后端错误!'
                    });
                })
                console.log('校验是否签到')
            }

            if (token && this.$route.path === '/home') {
                this.anno()
                console.log('弹出公告')
            }
        },
        mounted() {
            var that = this;
            Util.$on('demo', function (msg) {
                that.logout()
            })
        }

    }


</script>

<style scoped>
    .header-avatar {
        margin-top: 5px;
        float: right;
        width: 200px;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    .item {
        margin-top: 5px;
    }
</style>