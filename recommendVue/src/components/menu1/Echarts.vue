<template>
  <div id="myChart" :style="{width: '300px', height: '300px'}"></div>
</template>
<script>
// 引入基本模板
//let echarts = require('echarts/lib/echarts')
// 引入柱状图组件
require('echarts/lib/chart/bar')
// 引入提示框和title组件
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')
export default {
  name: "Echarts",
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  mounted(){
    this.drawLine();
  },
  methods: {
    drawLine(title){
      if(title!=0){
      let myChart = this.$echarts.init(document.getElementById('myChart'))
      // 绘制图表
      console.log(title)
      myChart.setOption({
        title: { text: title.title },
        tooltip: {},
        xAxis: {
          data:title.data.datax,
          "axisLabel":{
            interval: 0
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            margin: 2,
            formatter: function (value) {
              if (value >= 10000 && value < 10000000) {
                value = value / 10000 + "万";
              } else if (value >= 10000000) {
                value = value / 10000000 + "千万";
              }
              return value;
            }
          },
        },
        series: [{
          name: title.property,
          type: 'bar',
          data: title.data.datay
        }]
      });
    }
  }
  }
}

</script>

<style scoped>

</style>