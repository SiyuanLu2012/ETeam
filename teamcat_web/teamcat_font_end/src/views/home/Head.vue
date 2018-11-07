<template>
  <div class="app-body-head-default">
    <div class="app-body-header-bar-default">
      <div class="app-body-header-leftbar-default pull-left">
        <ul class="app-body-head-menu">

          <router-link to="/home/summary" tag="li" active-class="app-body-head-menu-item-active" class="app-body-head-menu-item">
            <a href="/home/summary"><i class="fa fa-fw  fa-bus"></i>面板</a>
          </router-link>
          <!--<li class="app-body-head-menu-item">-->
            <!--<a  href="/home/project/all"><i class="fa fa-flag fa-fw fa-lg"></i> <span>项目</span></a>-->
          <!--</li>-->
          <li class="app-body-head-menu-item">
            <a  href="/home/issue/1"><i class="fa fa-flag fa-fw fa-lg"></i> <span>问题</span></a>
          </li>
          <router-link to="/home/my/fortesting" tag="li" active-class="app-body-head-menu-item-active" class="app-body-head-menu-item">
            <a href="#"><i class="fa fa-fw  fa-flag"></i>提测</a>
          </router-link>
          <router-link to="/home/my/task" tag="li" active-class="app-body-head-menu-item-active" class="app-body-head-menu-item">
            <a href="/home/my/task"><i class="fa fa-fw  fa-bus"></i>任务</a>
          </router-link>
          <li name="header_menu_device" label="device" labelid="3" class="app-body-head-menu-item">
            <a href="/home/device/all"><i class="fa fa-fw fa-lg fa-mobile"></i>设备</a>
          </li>
          <li class="app-body-head-menu-item">
            <a  href="/home/webapps/all"><i class="fa fa-flag fa-fw fa-lg"></i> <span>工具</span></a>
          </li>
        </ul>
    </div>
      <div v-if="showNewButton" class="app-body-header-rightbar-default pull-right">
            <span @click="newTask">
              <Avatar style="background-color: #32be77;"  class="cursor-hand" icon="md-add" />
            </span>
      </div>
  </div>
  </div>
</template>

<script>
  import { mapMutations } from 'vuex'
  export default {
    name: 'MyHead',
    computed: {
      showNewButton: function () {
        if (this.$route.name === 'homeTask' || this.$route.name === 'homeFortesting') {
          return true
        }
        else {
          return false
        }
      }
    },
    methods: {
    ...mapMutations('projectglobal',['setCreateDialogShow']),
      newTask () {
        this.setCreateDialogShow(true)
      },
    },
    mounted: function () {
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
@import '../../components/layout/appBody';
@import '../../assets/teamcat/global/less/global';
</style>
