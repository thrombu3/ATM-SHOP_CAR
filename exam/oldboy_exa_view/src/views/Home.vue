<template>
    <div style="height: 100%">
        <el-container style="height: 100%">
            <el-header class="el-header">
                <Header/>
            </el-header>
            <el-container style="height: 100%">
                <el-aside width="225px" style="height: 100%">
                    <LeftTool/>
                </el-aside>
                <el-main>
                    <Main v-if="this.$route.path==='/home'"/>
                    <StudentTestBank v-if="this.$route.path==='/studentTestBank'"/>
                    <StudentPaper v-if="this.$route.path==='/studentPaper'"/>
                    <StudentSource v-if="this.$route.path==='/studentSource'"/>
                    <Subjects v-if="this.$route.path==='/subjects'"/>
                    <TeacherPaper v-if="this.$route.path==='/teacherPaper'"/>
                    <ChangePassword v-if="this.$route.path==='/changepwd'"/>
                    <TeacherTestBank v-if="this.$route.path==='/teacherTestBank'"/>
                    <!--                    教师题库操作预览题库-->
                    <TestBankView v-if="this.$route.path==='/teacherTestBank/testBankView'"/>
                    <MySign v-if="this.$route.path==='/myLater'"/>
                    <UploadNotes v-if="this.$route.path==='/upload_notes'"/>
                    <ExamView v-if="this.$route.path==='/studentTestBank/examView'"/>
                    <PaperView v-if="this.$route.path==='/studentTestBank/paperView'"/>
                    <SetPaperView v-if="this.$route.path==='/studentTestBank/setPaperView'"/>
                    <SourceView v-if="this.$route.path==='/studentTestBank/sourceView'"/>
                    <EditPaperView v-if="this.$route.path==='/teacherTestBank/editPaperView'"/>

                    <SourceShow v-if="this.$route.path==='/sourceShow'"/>




                </el-main>
            </el-container>
            <Translation/>
            <NowTime/>
        </el-container>
    </div>
</template>

<script>
    import Header from "../components/common/Header";
    import LeftTool from "../components/common/LeftTool";
    import Main from "../components/common/Main";
    import NowTime from "../components/common/NowTime";
    import Translation from "../components/common/Translation";
    import StudentTestBank from "../views/paper/StudentTestBank";
    import StudentPaper from "../views/paper/StudentPaper";
    import StudentSource from "../views/paper/StudentSource";
    import TeacherTestBank from "../views/paper/TeacherTestBank";
    import TeacherPaper from "../views/paper/TeacherPaper";
    import Subjects from "../views/paper/Subjects";
    import ChangePassword from "../components/common/ChangePassword";
    import TestBankView from "./paper/teacher/TestBankView";
    import MySign from "../components/students/MySign";
    import UploadNotes from "../components/students/UploadNotes";
    import ExamView from "./paper/student/ExamView";
    import PaperView from "./paper/student/PaperView";
    import SetPaperView from "./paper/student/SetPaperView";
    import SourceView from "./paper/student/SourceView";
    import EditPaperView from "./paper/teacher/EditPaperView";
    import SourceShow from "../components/common/SourceShow";

    export default {
        name: "Home",
        data() {
            return {}
        },
        components: {
            Header,
            LeftTool,
            NowTime,
            Main,
            StudentPaper,
            StudentSource,
            StudentTestBank,
            TeacherTestBank,
            Subjects,
            ChangePassword,
            TeacherPaper,
            TestBankView,
            MySign,
            Translation,
            UploadNotes,
            ExamView,
            PaperView,
            SetPaperView,
            SourceView,
            EditPaperView,

            SourceShow,



        },
        mounted() {
            // console.log(this.$route.path)
        },
    }
</script>

<style scoped>
    .el-header {
        background-color: #5bc0de;
        color: #deefeb;
        text-align: center;
        line-height: 50px;
    }
</style>