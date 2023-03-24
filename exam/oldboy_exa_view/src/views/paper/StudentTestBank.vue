<template>
    <div class="box">
        <el-container>
            <el-header height="50px">
                <div class="header pull-left">
                    <div>
                        <i class="el-icon-star-on"></i>
                        题库
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
                            prop="title"
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
                            :formatter="cDateFormat"
                            prop="date_time"
                            label="创建时间"
                            width="150">
                    </el-table-column>
                    <el-table-column
                            prop="teachers_name"
                            label="出题老师"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            :formatter="sDateFormat"
                            prop="exam_end_time"
                            label="考试截止时间"
                            width="200">
                    </el-table-column>
                    <el-table-column
                            label="是否开考"
                            width="100">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_start">
                                已开考
                            </span>
                            <span v-else>
                                未开考
                            </span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="是否结束"
                            width="100">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_end">
                                已结束
                            </span>
                            <span v-else>
                                未结束
                            </span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            align="center"
                            label="操作">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_start && scope.row.is_end">
                                <el-button type="info" size="small" disabled>考试已结束</el-button>
                            </span>
                            <span v-if="scope.row.is_start && !scope.row.is_end && !exam_commit">
                                <el-button type="primary" size="small" @click="handleRedirect(`/studentTestBank/examView?test_bank_id=${scope.row.id}`)">开始考试</el-button>
                            </span>
                            <span v-if="!scope.row.is_start && !scope.row.is_end">
                                <el-button type="info" size="small" disabled>考试未开始</el-button>
                            </span>
                            <span v-if="exam_commit && !scope.row.is_end">
                                <el-button type="info" size="small" disabled>考卷已提交</el-button>
                            </span>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        name: "StudentTestBank",
        data() {
            return {
                tableData: [],
                students_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
                exam_commit: false,
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
                duration: 1500,
                message: '加载数据中'
            });
            this.initialize()
        },
        methods: {
            // 初始化页面
            initialize() {
                // 'http://127.0.0.1:8000/students/test-bank/'
                this.$axios.get(this.$settings.base_url + `students/test-bank/?role_id=${this.role_id}`,{
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    console.log(response.data)
                    this.tableData = response.data
                }).catch(error => {
                    console.log(error)
                })
            },

            // 时间格式化
            cDateFormat(row, column) {
                // console.log(row, column)
                var date = row[column.property];
                if (date == undefined) {
                    return "";
                }
                return this.$moment(date).format("YYYY年MM月DD日");
            },
            sDateFormat(row, column) {
                // console.log(row, column)
                // console.log(row)
                var is_start = row.is_start
                if (!is_start) {
                    return '未开考'
                }
                var date = row[column.property];
                if (date == undefined) {
                    return "";
                }
                return this.$moment(date).format("YYYY年MM月DD日 HH:mm:ss");
            },

            // 跳转到考试页面
            handleRedirect(url) {
                this.$router.push(url)
            },


        }
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