<template>
    <transition name="el-fade-in-linear">


        <div v-show="show" class="start">
            <div id="bg">
                <p class="school"><span class="glyphicon glyphicon-leaf" aria-hidden="true"></span> 老男孩教育</p>
                <div class="jumbotron main">
                    <p class="title">考试管理系统</p>
                    <br><br>
                    <el-button type="success" @click="student_login">学生登录</el-button>
                    <el-button type="primary" @click="teacher_login">老师登录</el-button>
                    <el-button type="info" @click="admin_login">管理员登录</el-button>
                    <StudentLogin v-if="is_student_login" @close="close_login"/>
                    <TeacherLogin v-if="is_teacher_login" @close="close_login"/>
                    <AdminLogin v-if="is_admin_login" @close="close_login"/>
                </div>
<!--                <NowTime/>-->
                <el-row class="footer">
                    <el-col>
                        <p class="msg2">版权所有 ©2021 保留所有权利</p>
                    </el-col>
                </el-row>
            </div>
        </div>
    </transition>
</template>

<script>
    import StudentLogin from "../components/common/StudentLogin";
    import AdminLogin from "../components/common/AdminLogin";
    import TeacherLogin from "../components/common/TeacherLogin";
    import NowTime from "../components/common/NowTime";

    export default {
        name: "Start",
        data() {
            return {
                is_student_login: false,
                is_teacher_login: false,
                is_admin_login: false,
                show: false,

            }
        },
        components: {
            StudentLogin,
            AdminLogin,
            TeacherLogin,
            NowTime,
        },
        methods: {
            student_login() {
                this.is_student_login = true
            },
            teacher_login() {
                this.is_teacher_login = true
            },
            admin_login() {
                this.is_admin_login = true
            },
            close_login() {
                this.is_student_login = false;
                this.is_teacher_login = false;
                this.is_admin_login = false
            },
        },
        mounted() {
            // 校验是否登录
            let is_verify = this.$cookies.get('is_verify')
            if (is_verify) {
                this.$message('要是你执意这么做,你可以选择退出登录')
                this.$router.push('home')
            }
            this.show = true
        }
    }
</script>

<style scoped>
    .main {
        margin-top: 50px;
        margin-left: 525px;
        width: 500px;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.8);
    }

    .start {
        transition: all 1500ms;
    }

    .main > p {
        font-size: 50px;
    }

    .start #bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        overflow-y: auto;
        height: 100%;
        background: url("../assets/img/background.jpg") center top / cover no-repeat;
        background-color: rgba(179, 185, 203, 0.82) !important;
    }

    .school {
        margin-top: 20px;
        color: #dbe8e8;
        font-size: 100px;
        text-align: center;
    }

    .title {
        color: #ec971f;
    }

    .footer {
        margin-top: 50px;
        text-align: center;
    }

    .footer .msg2 {
        font-size: 14px;
        color: #e0dede;
        margin-top: 150px;
    }
</style>