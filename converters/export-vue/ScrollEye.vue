<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="m8,21c-1.1,0-2-.9-2-2V5c0-1.1-.9-2-2-2s-2,.9-2,2v3h4" /><path d="m8,21h2" /><path d="m20,12v-7c0-1.1-.9-2-2-2H4" /><path d="m13,18.8s1.64-3.21,4.5-3.21,4.5,3.21,4.5,3.21c0,0-1.64,3.21-4.5,3.21s-4.5-3.21-4.5-3.21Z" /><path d="m17.5,19.3c.28,0,.5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5Z" stroke-width="1.56"/>
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>