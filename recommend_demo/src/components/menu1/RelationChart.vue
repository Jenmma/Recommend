<template>
  <div id="relation">
    <div id="relationChart"></div>  
  </div>
</template>

<script>
// @ is an alias to /src
//按需引入 echarts 相关依赖
import * as echarts from "echarts/core";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from "echarts/components";
import { GraphChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";

echarts.use([
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GraphChart,
  CanvasRenderer,
]);

export default {
  name: "RelationChart",
  methods: {
    drawChart(graph) {
      let chartDom = document.getElementById("relationChart");
      let myChart = echarts.init(chartDom);
      let option;

      graph.nodes.forEach(function (node) {
        node.label = {
          show: node.symbolSize > 30,
        };
      });
      option = {
        title: {
          text: "Les Miserables",
          subtext: "Default layout",
          top: "bottom",
          left: "right",
        },
        tooltip: {},
        legend: [
          {
            // selectedMode: 'single',
            data: graph.categories.map(function (a) {
              return a.name;
            }),
          },
        ],
        animationDuration: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            name: "Les Miserables",
            type: "graph",
            layout: "force",
            data: graph.nodes,
            links: graph.links,
            categories: graph.categories,
            roam: true,
            label: {
              position: "right",
              formatter: "{b}",
            },
            force: {
                    repulsion: 80
                },
            lineStyle: {
              color: "source",
              curveness: 0.3,
            },
            emphasis: {
              focus: "adjacency",
              lineStyle: {
                width: 10,
              },
            },
          },
        ],
      };

      myChart.setOption(option);
    },
  },
  computed: {
    defaultActive() {
      return "/" + this.$route.path.split("/").reverse()[0];
    },
  },
  mounted: function () {
    console.log("mounted:here");
  }
};
</script>

<style scoped>
#relationChart {
  width: 900px;
  height: 450px;
}
</style>
