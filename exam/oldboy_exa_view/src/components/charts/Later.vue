<template>
    <div style="width: 1260px">
        <hr>
        <br>
        <el-button plain @click="table = true" style="float: right; margin-right: 6%; font-weight: bold">近日迟到学员一览
        </el-button>
        <el-button plain @click="myLater" style="float: right; margin-right: 5%; font-weight: bold">我的签到情况
        </el-button>
        <el-drawer

                title="近日迟到学员一览"
                :visible.sync="table"
                direction="rtl"
                size="30%"
                style="font-size: 20px; font-weight: bold;"
        >
            <el-table
                    v-loading="loading"
                    :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
                    :default-sort="{prop: 'date', order: 'descending'}"
                    style=""
            >
                <el-table-column prop="date" label="日期" sortable width="120"></el-table-column>
                <el-table-column prop="name" label="姓名" sortable width="120"></el-table-column>
                <el-table-column align="right">
                    <template slot="header" slot-scope="scope">
                        <el-input
                                v-model="search"
                                size="mini"
                                style="font-weight: lighter"
                                placeholder="输入关键字搜索"/>
                    </template>
                </el-table-column>
            </el-table>
        </el-drawer>


        <!--        <el-table-->
        <!--                :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"-->
        <!--                style="width: 400px; margin-left: 3%"-->
        <!--                :default-sort="{prop: 'date', order: 'descending'}"-->
        <!--        >-->
        <!--            <el-table-column-->
        <!--                    prop="date"-->
        <!--                    label="日期"-->
        <!--                    sortable-->
        <!--                    width="120">-->
        <!--            </el-table-column>-->
        <!--            <el-table-column-->
        <!--                    prop="name"-->
        <!--                    label="姓名"-->
        <!--                    sortable-->
        <!--                    width="120">-->
        <!--            </el-table-column>-->
        <!--            <el-table-column-->
        <!--                    align="right">-->
        <!--                <template slot="header" slot-scope="scope">-->
        <!--                    <el-input-->
        <!--                            v-model="search"-->
        <!--                            size="mini"-->
        <!--                            style="font-weight: lighter"-->
        <!--                            placeholder="输入关键字搜索"/>-->
        <!--                </template>-->
        <!--            </el-table-column>-->
        <!--        </el-table>-->
    </div>
</template>

<script>
    export default {
        name: "Later",
        data() {
            return {
                tableData: [{data: ''}, {name: ''}],
                loading: true,
                search: '',
                table: false,

            }
        },
        methods: {
            myLater() {
                this.$router.push('/myLater')
            }
        },
        created() {
            this.$axios.get(`${this.$settings.base_url}students/get_sign_all/`
            ).then(response => {
                if (response.data.status == 100) {
                    this.$axios.post(`${this.$settings.base_url}students/get_sign_all/`,
                        {
                            signInfo: response.data.data_all
                        }).then(item => {
                        console.log(item.data.data_all)
                        this.tableData = item.data.data_all
                        this.loading= false
                    }).catch(() => {
                        this.$message({
                            message: '后端错误!'
                        });
                    })
                }
            }).catch(() => {
                this.$message({
                    message: '后端错误!'
                });
            })
        }
    }
</script>

<style scoped>

</style>