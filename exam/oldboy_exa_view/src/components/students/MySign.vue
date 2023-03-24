<template>
    <!--为echarts准备一个具备大小的容器dom-->
    <div style="width: 1260px">
        <div style="width: 40%; margin-top: 80px; float: left; margin-left: 4%;">
            <h2 style="text-align: left; font-size: large; font-weight: bold">签到详情</h2>
            <br>
            <el-calendar>
                <!-- 这里使用的是 2.5 slot 语法，对于新项目请使用 2.6 slot 语法-->
                <template
                        slot="dateCell"
                        slot-scope="{date, data}">
                    <p>{{ data.day.split('-').slice(2).join('-') }}</p>
                    <br>
                    <div v-for="item in data_list">
                        <div v-if="(item.months).indexOf(data.day.split('-').slice(1)[0])!=-1">
                            <div v-if="(item.days).indexOf(data.day.split('-').slice(2).join('-'))!=-1">
                                <el-tooltip class="item" effect="dark" :content="item.things" placement="right">
                                    <div class="is-selected">{{ '✔️'}}</div>
                                </el-tooltip>
                            </div>
                            <div v-else></div>
                        </div>
                        <div v-else></div>
                    </div>
                </template>
            </el-calendar>
        </div>
        <div id="main" style="width: 560px;height: 450px; margin-top: 80px; float: right; margin-right: 6%"></div>
    </div>
</template>
<script>
    export default {
        name: '',
        data() {
            return {
                charts: '',
                data_list: [],
            }
        },
        methods: {
            getSignNum() {
                let opinion = ['签到', '迟到']
                let opinionData = [
                    {value: '', name: '签到'},
                    {value: '', name: '迟到'},
                ]
                this.$axios.get(`${this.$settings.base_url}students/get-signnum/`, {
                    params: {user_id: this.$cookies.get('user_id')}
                }).then(res => {
                    opinionData[0].value = res.data.data_all.sign_num
                    opinionData[1].value = res.data.data_all.no_sign_num
                    this.drawPie('main', opinion, opinionData)
                }).catch(() => {
                    this.$message({
                        message: '后端错误!'
                    });
                })
            },
            drawPie(id, opinion, opinionData) {
                this.charts = this.$echarts.init(document.getElementById(id))
                this.charts.setOption({
                    title: {
                        text: '个人签到数据',
                        subtext: '数据来自于当日',
                        left: 'center',
                    },
                    tooltip: {
                        trigger: 'item',
                    },
                    legend: {
                        bottom: '1px',
                        left: 'center',
                        data: opinion
                    },
                    series: [
                        {
                            name: '个人数据',
                            type: 'pie',
                            radius: ['20%', '75%'],
                            avoidLabelOverlap: false,
                            label: {
                                normal: {
                                    show: false,
                                    position: 'center'
                                },
                                emphasis: {
                                    show: true,
                                    textStyle: {
                                        fontSize: '30',
                                        fontWeight: 'blod'
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    show: false
                                }
                            },
                            data: opinionData
                        }
                    ]
                })
            }
        },
        created() {
            this.$axios.get(`${this.$settings.base_url}students/get-signdata/`, {
                params: {user_id: this.$cookies.get('user_id')}
            }).then(res => {
                this.data_list = res.data.data_all
                console.log(this.data_list)
            }).catch(() => {
                this.$message({
                    message: '后端错误!'
                });
            })
        },
        //调用
        mounted() {
            this.getSignNum()
        }
    }
</script>
<style scoped>
    * {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    .is-selected {
        color: #1989FA;
    }

</style>