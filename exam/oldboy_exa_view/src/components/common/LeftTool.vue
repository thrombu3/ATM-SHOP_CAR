<template>
    <div style="height: 100%">
        <el-menu
                router
                :default-active="this.$route.path"
                class="el-menu-vertical-demo"
                @select="handleSelect">
            <!--                @open="handleOpen"-->
            <!--                @close="handleClose"-->
            <el-menu-item index="/home">
                <i class="el-icon-location"></i>
                <span slot="title">首页</span>
            </el-menu-item>
            <el-menu-item index="/sourceShow">
                <i class="el-icon-location"></i>
                <span slot="title">成绩展示</span>
            </el-menu-item>
            <el-submenu index="1">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span>在线考试</span>
                </template>
                <el-menu-item v-for="(item,i) in navStudentList" :key="i" :index="item.name">
                    {{item.navItem}}
                </el-menu-item>
                <!--                <el-menu-item index="1-1">选项1</el-menu-item>-->
                <!--                <el-menu-item index="1-2">选项2</el-menu-item>-->
                <!--                <el-menu-item index="1-3">选项3</el-menu-item>-->
            </el-submenu>

            <el-submenu index="2">
                <template slot="title">
                    <i class="el-icon-menu"></i>
                    <span slot="title">考试管理</span>
                </template>
                <el-menu-item v-for="(item,i) in navTeacherList" :key="i" :index="item.name">
                    {{item.navItem}}
                </el-menu-item>
            </el-submenu>


            <!--            <el-menu-item index="3" disabled>-->
            <!--                <i class="el-icon-document"></i>-->
            <!--                <span slot="title">导航三</span>-->
            <!--            </el-menu-item>-->
            <!--            <el-menu-item index="4">-->
            <!--                <i class="el-icon-setting"></i>-->
            <!--                <span slot="title">导航四</span>-->
            <!--            </el-menu-item>-->
        </el-menu>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                navStudentList: [
                    {name: '/studentTestBank', navItem: '题库'},
                    {name: '/studentPaper', navItem: '考卷'},
                    {name: '/studentSource', navItem: '考试成绩'},
                ],
                navTeacherList: [
                    {name: '/teacherTestBank', navItem: '题库操作'},
                    {name: '/subjects', navItem: '试题操作'},
                    {name: '/teacherPaper', navItem: '考卷操作'},
                ]
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                // console.log(key, keyPath);
            },
            // handleOpen(key, keyPath) {
            //     console.log(key, keyPath);
            // },
            // handleClose(key, keyPath) {
            //     console.log(key, keyPath);
            // },
        },
        created() {

        }
    }
</script>

<style>
    .el-menu-vertical-demo {
        width: 225px;
        height: 100%;
    }
</style>