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
    <path d="m12,2v2h-6c-1.1,0-2,.9-2,2v12c0,1.1.9,2,2,2h6v2" /><rect x="8" y="8" width="8" height="8" rx="1.96" ry="1.96" />
  </svg>
</template>

<script setup>
  const props = defineProps({
    size: { type: [String, Number], default: 24 },
    stroke: { type: [String, Number], default: 1.5 },
  });
</script>

<style lang="scss" scoped></style>