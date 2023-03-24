<template>

    <div class="echarts">
        <SignNumber/>
        <Later/>



        <!--        <div style="width: 500px; float: right">-->
        <!--            <el-dropdown>-->
        <!--              <span class="el-dropdown-link">-->
        <!--                {{course_name}}<i class="el-icon-arrow-down el-icon&#45;&#45;right"></i>-->
        <!--              </span>-->
        <!--                <el-dropdown-menu slot="dropdown">-->
        <!--                    <el-dropdown-item>Linux</el-dropdown-item>-->
        <!--                    <el-dropdown-item>Python</el-dropdown-item>-->
        <!--                </el-dropdown-menu>-->
        <!--            </el-dropdown>-->
        <!--        </div>-->

    </div>


</template>

<script>
    import SignNumber from "../charts/SignNumber";
    import Later from "../charts/Later";

    export default {
        name: 'Main',
        components: {
            SignNumber,
            Later,
        },
        data() {
            return {
            }
        },
        methods: {

        },
        mounted() {

        },
    }
</script>

<style scoped>

</style>