<template>
    <div class="box">
        <el-container>
            <el-header height="50px">
                <div class="header pull-left">
                    <div>
                        <i class="el-icon-star-on"></i>
                        已批阅的考卷
                    </div>
                </div>
            </el-header>
            <el-main>
                <el-table
                        :data="tableData"
                        border
                        style="width: 100%">
                    <el-table-column
                            align="center"
                            type="index"
                            label="序号"
                            width="50">
                        <template slot-scope="scope">
                            <span>{{scope.$index+1}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            prop="test_bank_name"
                            label="题库名"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="题数"
                            width="50">
                        <template slot-scope="scope">
                            <span>{{scope.row.subjects_list.length}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            :formatter="dateFormat"
                            prop="commit_time"
                            label="考卷提交时间"
                            width="200">
                    </el-table-column>
                    <el-table-column
                            prop="teachers_name"
                            label="批阅老师"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="成绩"
                            width="100">
                        <template slot-scope="scope">
                            <span>{{scope.row.source}}</span>
                        </template>
                    </el-table-column>
                    <!--                    要不要都行-->
                    <el-table-column
                            label="题库状态"
                            width="130">
                        <el-button type="info" size="small" disabled>已结束</el-button>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="操作">
                        <template slot-scope="scope">
                            <el-button type="primary" size="small"
                                       @click="handleRedirect(`/studentTestBank/sourceView?paper_id=${scope.row.id}`)">
                                查看考卷
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "StudentSource",
        data() {
            return {
                tableData: [],
            }
        },
        mounted() {
            // 权限校验
            // let role_id = this.$cookies.get('role_id')
            // if (role_id != '2') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是学生,没有权限'
            // });
            //     this.$router.go(-1)
            // }
            this.$message({
                type: 'info',
                duration: 500,
                message: '加载数据中'
            });
            // 'http://127.0.0.1:8000/students/student-paper/?student_id=1&is_check=True'
            let students_id = this.$cookies.get('user_id');
            this.$axios.get(this.$settings.base_url + `students/student-paper/?is_check=True&student_id=${students_id}`).then(response => {
                console.log(response.data)
                this.tableData = response.data
            }).catch(error => {
                console.log(error)
            })
        },
        methods: {
            // 时间格式化
            dateFormat(row, column) {
                // console.log(row, column)
                var date = row[column.property];
                if (date == undefined) {
                    return "";
                }
                return this.$moment(date).format("YYYY年MM月DD日 HH:mm:ss");
            },

            // 跳转到查看有成绩的试卷页面
            handleRedirect(url) {
                this.$router.push(url)
            },


        },
    }
</script>

<style scoped>
    .box {
        height: 100%;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)
    }

    .header {
        font-size: 20px;
        font-weight: normal;
        margin-top: 20px;
    }
</style>