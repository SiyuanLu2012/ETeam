<template>
  <div :id="task.id"  @click="onViewTask" :key="task.id">
  <Card  :padding="0"  class="board-column-item cursor-hand" :style="'border-left: 1px solid '+task.PriorityFormator">
    <div class="board-item-body">
      <div>{{ task.Title }}</div>
      <div style="position: absolute;bottom:2px;right:10px;font-size: 10px;color:gray">{{ task.DeadLineFormat }}</div>
    </div>
    <div class="board-item-rightbar">
      <div class="board-item-avatar">
        <Avatar style="background-color:#388E8E">{{ task.OwnerName }}</Avatar>
      </div>
      <!--<Badge count="10"></Badge>-->

    </div>
  </Card>
  </div>
</template>

<script>

  export default {
    name: 'ProjectTaskItem',
    props: ['task'],
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    methods: {
      onTaskItemClick (event) {
        this.setCreateDialogShow(true)
        let taskID = event.target.getAttribute('id')
        this.taskItemID = parseInt(taskID)
      },
      onViewTask (event) {
        this.$emit('view-task', this.task.id)
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
  .board-item-rightbar {
    display: inline-table;
  }

  .board-item-avatar {
    margin-right: 15px;
    margin-top: 10px;
  }
  .board-column-item {
    margin-bottom: 5px;
    margin-top: 5px;
    min-height: 74px;
    max-height: 200px;
    width: 280px;
  }

  .board-item-priority {
    width: 1px;
    display: inline-block;
    float: left;
    height:170px;
  }

  .board-item-body {
    width: 235px;
    display: inline-table;
    word-wrap: break-word;
    white-space: initial;
    padding: 10px;

  }

</style>
