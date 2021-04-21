<template>
  <div id="main1" style="float:right;width:100%;height: 350px"></div>
</template>

<script>// 引入基本模板
let echarts = require('echarts/lib/echarts')
// 引入饼状图组件
require('echarts/lib/chart/pie')
// 引入提示框和title组件
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')


export default {
  name: "bingzhuangtu",
  mounted(){
    this.initData();
  },
  methods:{
    //初始化数据
    initData(bing) {
      // 基于准备好的dom，初始化echarts实例
      console.log("this is bing")
      console.log(bing)
      var myChart = echarts.init(document.getElementById('main1'));
      // 绘制图表
      myChart.setOption({
        title : {
          text: bing.title,//主标题
          //subtext: '纯属虚构',//副标题
          x:'center',//x轴方向对齐方式
        },
        tooltip : {
          trigger: 'item',
          formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        legend: {
          orient: 'vertical',
          bottom: 'bottom',
          data: bing.dataname,
        },
        series : [
          {
            name: '分布',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
           data:bing.abstdata,
            itemStyle: {
              emphasis: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      });
    },
  }
}
</script>