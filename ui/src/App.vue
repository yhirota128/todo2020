<template>
    <div>
        <h1>ToDo</h1>
        <input v-model="newTaskText">
        <button @click="addTask">追加</button>
        <task-list :tasks="tasks" @delete-task="deleteTask"/>
    </div>
</template>

<script>
    import axios from 'axios';
    import TaskList from './components/TaskList';

    const API_HOST = 'http://localhost:8000';

    export default {
        name: 'App',
        components: {
            TaskList
        },
        data() {
            return {
                newTaskText: '',
                tasks: []
            };
        },
        mounted() {
            this.getTasks();
        },
        methods: {
            async getTasks() {
                const response = await axios.get(API_HOST + '/tasks');
                this.tasks = response.data;
            },
            async addTask() {
                const params = {
                    task_text: this.newTaskText
                };
                await axios.post(API_HOST + '/tasks', params);
                this.newTaskText = '';
                this.getTasks();
            },
            async deleteTask(task) {
                const params = {
                    status: 1
                };
                await axios.post(API_HOST + '/tasks/' + task.id, params);
                this.getTasks();
            },
        }
    }
</script>

<style>
</style>
