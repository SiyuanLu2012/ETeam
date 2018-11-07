<template>
  <div>
    <board-column v-for="tasklist in taskForColumns" :key="tasklist.id" :columnID="tasklist.id" :group="tasklist.group"
                  v-bind:itemList.sync="tasklist.data" :columnTitle="tasklist.title+'-'+tasklist.count"
                  style="margin-left: 10px;" @end="onEnd" @reachBottom="onReachBottom">
      <template slot-scope="slotProps">
         <project-task-item :task="slotProps.element" @view-task="onViewTask"></project-task-item>
      </template>
    </board-column>
    <project-task-create-dialog :taskID="taskItemID"></project-task-create-dialog>
  </div>
</template>

<script>
  import draggable from 'vuedraggable'
  import { mapGetters, mapMutations } from 'vuex'
//  import store from '../../store/project/task'
  import BoardColumn from '../../../components/common/BoardColumn.vue'
  import ProjectTaskCreateDialog from './ProjectTaskCreateDialog.vue'
  import ProjectTaskItem from './ProjectTaskItem.vue'
  import { axiosSync } from './ProjectTask'

  export default {
    name: 'projectTaskList',
    props: {
      projectID: {
        type: [Number,String],
        defalut: 0
      }
    },
    data () {
      return {
        columnItemHeight: 200,
        taskList: [],
        taskItemID: 0
      }
    },
    computed: {
      ...mapGetters('task', ['taskChange']),
      ...mapGetters('projectglobal', ['projectVersion']),
      versionID: function () {
        return this.projectVersion
      },
      taskForColumns: function () {
        if (this.taskChange === true)
        {
          this.taskList = this.getColumnTasks()
          this.setTaskChange(false)
        }
        return this.taskList
      },
      project: function () {
        let result = 0
        if( this.projectID )
        {
           result = this.projectID
        }
        return result
      }

    },
    methods:
      {
        ...mapMutations('task', ['setTaskChange']),
        ...mapMutations('projectglobal', ['setViewDialogShow']),
        getColumnTasks () {
          let result=[]
          let waitForTasks = {id: 0, title: '待处理', group: 'ProjectTask', page: 1, count: 0, data: []}
          let processTasks = {id: 1, title: '处理中', group: 'ProjectTask', page: 1, count: 0, data: []}
          let finishedTasks = {id: 2, title: '已完成', group: 'ProjectTask', page: 1, count: 0, data: []}
          let pauseTasks = {id: 3, title: '已暂停', group: 'ProjectTask', page: 1, count: 0, data: []}
          result.push(waitForTasks)
          result.push(processTasks)
          result.push(finishedTasks)
          result.push(pauseTasks)
          for (let i = 0; i < result.length; i++)
          {
            let tempData = this.getTaskList(this.project,this.versionID,result[i].id, result[i].page)
            tempData.then(function (value) {
              result[i].data = value.data.result.results
              result[i].count = value.data.result.count
            })
          }
          return result
        },
        onStart () {
          console.log('start')
        },
        onEnd (evt) {
          let toID = evt.to.getAttribute('id')
          let fromID = evt.from.getAttribute('id')
          let itemOldIndex = evt.oldIndex
          let itemNewIndex = evt.newIndex
          let itemID = evt.item.getAttribute('id')
          this.alterColumnData(fromID, toID, itemID, itemOldIndex, itemNewIndex)
          this.$axios.patch('/api/project/task/'+itemID+'/',{'Status': toID}).then(response => {
             console.log(response)
          }, response => {
            this.setTaskChange(true)

          })

        },

        onRemove () {
          console.log('remove')
        },
        onMove () {
          console.log('move')
        },
        alterColumnData (fromID, toID, itemID, itemOldIndex, itemNewIndex) {
          let dragItem= null
          this.taskForColumns.forEach(function (taskList, index) {
             if(taskList.id === parseInt(fromID))
             {
               taskList.count=taskList.count-1
               for(let i=0; i<taskList.data.length; i++) {
                 if(taskList.data[i].id === parseInt(itemID))
                 {
                   dragItem=taskList.data[i]
                   taskList.data.splice(i, 1)
                   break
                 }
               }
             }
          })

          this.taskForColumns.forEach(function (taskList, index) {
            if(taskList.id === parseInt(toID))
            {
              taskList.count=taskList.count+1
              taskList.data.splice(itemNewIndex,0,dragItem)
            }
          })
        },
        onReachBottom (columnid) {
          for( let i=0; i < this.taskForColumns.length; i++ ) {
            if (this.taskForColumns[i].id === parseInt(columnid)) {
              let moreTasks=[]
              let tasks=this.taskForColumns
              this.taskForColumns[i].page=this.taskForColumns[i].page+1
              let tempData = this.getTaskList(this.project,this.versionID,this.taskForColumns[i].id, this.taskForColumns[i].page)
              tempData.then(function (value) {

                moreTasks=value.data.result.results
                tasks[i].data.push(...moreTasks)
              })
              break
            }
          }
        },
        getTaskList  (projectID, versionID, status, page) {
          let url='/api/project/' + projectID + '/version/'+versionID+'/project_tasks?Status=' + status + '&page=' + page
          let result = axiosSync(url,{},'get')
          console.log(url)
          return result
        },
        onTaskItemClick (event) {
          this.setCreateDialogShow(true)
          let taskID = event.target.getAttribute('id')
          this.taskItemID = parseInt(taskID)
        },
        onViewTask (taskID)
        {
          this.setViewDialogShow(true)
          this.taskItemID = parseInt(taskID)
//          console.log(this.taskItemID)
        }

      },
    created: function () {
      this.taskList = this.getColumnTasks()
    },
    mounted: function () {
    },
    watch: {
      versionID: function (value) {
        this.taskList = this.getColumnTasks()
      },

      projectID: function () {
        this.taskList = this.getColumnTasks()
      }
//      taskChange: function () {
//        this.taskForColumns = this.getColumnTasks()
//        this.setTaskChange(false)
//      }

    },

    components: {
      draggable,
      BoardColumn,
      ProjectTaskCreateDialog,
      ProjectTaskItem
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
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

  .board-item-rightbar {
    display: inline-table;
  }

  .board-item-avatar {
    margin-right: 15px;
    margin-top: 10px;
  }

</style>
