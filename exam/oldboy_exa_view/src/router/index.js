import Vue from 'vue'
import VueRouter from 'vue-router'
import Start from "../views/Start";
import Home from "../views/Home";
import StudentTestBank from "../views/paper/StudentTestBank";
import StudentPaper from "../views/paper/StudentPaper";
import StudentSource from "../views/paper/StudentSource";
import TeacherTestBank from "../views/paper/TeacherTestBank";
import TeacherPaper from "../views/paper/TeacherPaper";
import Subjects from "../views/paper/Subjects";
import ChangePassword from "../components/common/ChangePassword";
import UploadNotes from "../components/students/UploadNotes";


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Start',
        component: Start
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    // 题库
    {
        path: '/studentTestBank',
        name: 'StudentTestBank',
        component: Home
    },
    // 开始考试页面
    {
        path: '/studentTestBank/examView',
        name: 'ExamView',
        component: Home
    },
    // 预览考卷页面
    {
        path: '/studentTestBank/paperView',
        name: 'PaperView',
        component: Home
    },
    // 修改考卷页面
    {
        path: '/studentTestBank/setPaperView',
        name: 'SetPaperView',
        component: Home
    },
    // 查看考卷页面（有成绩）
    {
        path: '/studentTestBank/sourceView',
        name: 'SourceView',
        component: Home
    },
    {
        path: '/studentPaper',
        name: 'StudentPaper',
        component: Home
    },
    {
        path: '/studentSource',
        name: 'StudentSource',
        component: Home
    },
    // 题库操作
    {
        path: '/teacherTestBank',
        name: 'TeacherTestBank',
        component: Home
    },
    // 预览题库
    {
        path: '/teacherTestBank/testBankView',
        name: 'TestBankView',
        component: Home
    },
    // 批阅考卷
    {
        path: '/teacherTestBank/editPaperView',
        name: 'EditPaperView',
        component: Home
    },
    {
        path: '/subjects',
        name: 'Subjects',
        component: Home
    },
    {
        path: '/teacherPaper',
        name: 'TeacherPaper',
        component: Home
    },
    {
        path: '/changepwd',
        name: 'ChangePassword',
        component: Home
    },
    {
        path: '/sourceShow',
        name: 'SourceShow',
        component: Home
    },
    {
    path: '/myLater',
    name: 'MySign',
    component: Home
    },
    {
    path: '/upload_notes',
    name: 'UploadNotes',
    component: Home
    },


]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
