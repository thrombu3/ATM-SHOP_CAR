<template>
    <div class="box">
        <el-container>
            <el-header height="110px">
                <div class="header">
                    <i class="el-icon-star-on"></i>
                    <span>考卷</span>
                </div>
                <div class="header pull-left">
                    <el-form :model="form">
                        <el-form-item label="题库" label-width="100px">
                            <el-select v-model="form.test_bank" placeholder="请选择要看的题库">
                                <el-option :label="item.title" :value="item.id"
                                           v-for="item in this.testBank"></el-option>
                            </el-select>
                        </el-form-item>
                    </el-form>
                </div>
                <div class="header pull-left" style="margin-left: 10px">
                    <el-button icon="el-icon-search" circle @click="form.test_bank=''"></el-button>
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
                            <span>{{scope.$index+1+(page-1)*page_size}}</span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            prop="students_name"
                            label="考生名"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="teachers_name"
                            label="出题老师"
                            width="100">
                    </el-table-column>
                    <el-table-column
                            prop="test_bank_name"
                            label="题库名"
                            width="180">
                    </el-table-column>
                    <el-table-column
                            align="center"
                            prop="subjects_num"
                            label="题数"
                            width="50">
                    </el-table-column>
                    <el-table-column
                            :formatter="dateFormat"
                            prop="commit_time"
                            label="提交时间"
                            width="200">
                    </el-table-column>
                    <el-table-column
                            label="是否批阅"
                            width="100">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_check">
                                已批阅
                            </span>
                            <span v-else>
                                未批阅
                            </span>
                        </template>
                    </el-table-column>
                    <el-table-column
                            label="考试是否结束"
                            width="120">
                        <template slot-scope="scope">
                            <span v-if="scope.row.test_bank_is_end">
                                已结束
                            </span>
                            <span v-else>
                                未结束
                            </span>
                        </template>
                    </el-table-column>
<!--                    可以加一个成绩字段-->
                    <el-table-column
                            align="center"
                            label="操作">
                        <template slot-scope="scope">
                            <span v-if="scope.row.is_check && scope.row.test_bank_is_end">
                                <el-popover
                                        placement="bottom"
                                        title="成绩"
                                        width="200"
                                        trigger="click"
                                        :content='String(scope.row.source)'>
                                    <el-button slot="reference" type="primary" size="small">查看成绩</el-button>
                                </el-popover>
                                <!--                                <el-button type="primary" size="small"-->
                                <!--                                           @click="handleCheckSource(scope.row.id, scope.row.source)">查看成绩</el-button>-->
                            </span>
                            <span v-if="!scope.row.is_check && scope.row.test_bank_is_end">
                                <el-button type="primary" size="small"
                                           @click="handleRedirect(`/teacherTestBank/editPaperView?paper_id=${scope.row.id}`)">批阅考卷</el-button>
                            </span>
                            <span v-if="!scope.row.is_check && !scope.row.test_bank_is_end">
                                <el-button type="info" size="small" disabled>考试未结束</el-button>
                            </span>
                        </template>
                    </el-table-column>
                </el-table>
            </el-main>
        </el-container>
        <!--分页-->
        <div class="course_pagination block">
            <el-pagination
                    @size-change="handleSizeChange"
                    @current-change="handleCurrentChange"
                    :current-page.sync="page"
                    :page-sizes="[5, 8, 12, 15]"
                    :page-size="page_size"
                    layout="sizes, prev, pager, next"
                    :total="paper_total">
            </el-pagination>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TeacherPaper",
        data() {
            return {
                tableData: [],
                teachers_id: Number(this.$cookies.get('user_id')),
                role_id: this.$cookies.get('role_id'),
                token: this.$cookies.get('token'),
                page: this.$route.query.page ? this.$route.query.page : 1,
                page_size: this.$route.query.page_size ? this.$route.query.page : 5,
                paper_total: 0,

                testBank: [],
                form: {
                    'test_bank': ''
                },
            }
        },
        // 检测到里面的变量就会执行，和computed类似
        watch: {
            "page_size": function () {
                this.$message({
                    type: 'info',
                    duration: 1000,
                    message: '加载数据中'
                });
                this.initialize();
            },
            "page": function () {
                this.$message({
                    type: 'info',
                    duration: 1000,
                    message: '加载数据中'
                });
                this.initialize();
            },
            "form.test_bank": function () {
                this.$message({
                    type: 'info',
                    duration: 1000,
                    message: '加载数据中'
                });
                this.initialize();
            }
        },
        mounted() {
            // 权限校验
            // let role_id = this.$cookies.get('role_id')
            // if (role_id != '1') {
            //     this.$message({
            //     type: 'warning',
            //     duration: 1000,
            //     message: '你不是老师,没有权限'
            // });
            //     this.$router.go(-1)
            // }
            this.$message({
                type: 'info',
                duration: 500,
                message: '加载数据中'
            });

            this.$axios.get(this.$settings.base_url + `teachers/get_teachers_test_bank/?teachers=${this.teachers_id}&role_id=${this.role_id}`, {
                headers: {'Authorization': `jwt ${this.token}`}
            }).then(response => {
                this.testBank = response.data
            })

            this.initialize()
            // console.log(this.page)
            // console.log(this.page_size)
        },
        methods: {
            handleSizeChange(val) {
                // 每页数据量发生变化时执行的方法
                this.page = 1;
                this.page_size = val;
            },
            handleCurrentChange(val) {
                // 页码发生变化时执行的方法
                this.page = val;
            },

            // 时间格式化
            dateFormat(row, column) {
                // console.log(row, column)
                var date = row[column.property];
                if (date == undefined) {
                    return "";
                }
                return this.$moment(date).format("YYYY年MM月DD日 HH:mm:ss");
            },

            initialize() {
                // 'http://127.0.0.1:8000/teachers/teachers-paper/?teacher_id=1'
                this.$axios.get(this.$settings.base_url + `teachers/teachers-paper/?teacher_id=${this.teachers_id}&role_id=${this.role_id}&page=${this.page}&page_size=${this.page_size}&test_bank=${this.form.test_bank}`, {
                    headers: {'Authorization': `jwt ${this.token}`}
                }).then(response => {
                    // console.log(response.data)
                    this.tableData = response.data.results;
                    this.paper_total = response.data.count
                }).catch(error => {
                    console.log(error)
                })
            },

            // 查看成绩
            // handleCheckSource(id, source) {
            //
            // },

            // 跳转批阅考卷页面
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