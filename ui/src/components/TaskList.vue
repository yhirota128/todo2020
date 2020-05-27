<template>
    <ul>
        <li v-for="task in tasks" :key="task.id" :class="task.status === 0 ? '' : 'done'">
            {{ task.task_text }}
            <button v-if="task.status === 0" @click="$emit('delete-task', task)">完了</button>
        </li>
    </ul>
</template>

<script>
    export default {
        name: 'TaskList',
        props: ['tasks']
    }
</script>

<style scoped>

    .done {
        color: lightgray;
    }

</style>